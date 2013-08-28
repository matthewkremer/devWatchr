import pyinotify, os, os.path, devWatchr
from StringIO import StringIO

'''
	View Documentation here:
	https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/minifyJS.md
'''

def writeLoop(temp, directory, settings):
	in_files = os.listdir(directory)
	in_files.sort()
	
	if len(in_files) != 0:
		for f in in_files:
			if f[-3:] == '.js':
				fh = open('%s/%s' % (directory, f))
				data = fh.read() + '\n'
				fh.close()
				temp.write(data)
				print ' + %s' % f
			elif os.path.isdir(directory+'/'+f):
				if settings['recursive']:
					writeLoop(temp, directory+'/'+f, settings)

class minifyJS(devWatchr.watcher):
	def __init__(self, settings):
		self.settings = settings
		if 'recursive' not in self.settings:
			self.settings['recursive'] = False

	def _run(self,event):
		if not event.name[-3:] == ".js":
			return
		if (event.pathname.endswith('%s.js' % self.settings['minify_to']) or event.pathname.endswith('%s.min.js' % self.settings['minify_to'])):
                        return
		devWatchr.colors.printBlue('==> JS Modification Detected')

		js_path = event.path
		minify_to = self.settings['minify_to']
		verbose = False

		in_type='js'
		out_file = '%s/%s' % (js_path, '%s.min.js' % minify_to)
		debug_file = '%s/%s' % (js_path, '%s.js' % minify_to)
		
		try:
			os.remove(out_file)
			os.remove(debug_file)
		except OSError:
			pass
		
		temp = open(debug_file, 'w')
		writeLoop(temp, js_path, self.settings)
		temp.close()
			
		out = open(out_file, 'w')
		
		jsm = JavascriptMinify()
		jsm.minify(open(debug_file,'r'), out)
		
		out.close()
		
		org_size = os.path.getsize(debug_file)
		new_size = os.path.getsize(out_file)

		devWatchr.colors.printGreen('==> %s' % out_file)
		devWatchr.colors.printGreen('Original: %.2f kB' % (org_size / 1024.0))
		devWatchr.colors.printGreen('Compressed: %.2f kB' % (new_size / 1024.0))
		devWatchr.colors.printGreen('Reduction: %.1f%%' % (float(org_size - new_size) / org_size * 100))

handles = {
	'minifyJS': minifyJS
}

# This code is original from jsmin by Douglas Crockford, it was translated to
# Python by Baruch Even. The original code had the following copyright and
# license.
#
# /* jsmin.c
#	2007-05-22
#
# Copyright (c) 2002 Douglas Crockford  (www.crockford.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# The Software shall be used for Good, not Evil.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# */

def jsmin(js):
	ins = StringIO(js)
	outs = StringIO()
	new().minify(ins, outs)
	str = outs.getvalue()
	if len(str) > 0 and str[0] == '\n':
		str = str[1:]
	return str

def isAlphanum(c):
	"""return true if the character is a letter, digit, underscore,
		   dollar sign, or non-ASCII character.
	"""
	return ((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') or
			(c >= 'A' and c <= 'Z') or c == '_' or c == '$' or c == '\\' or (c is not None and ord(c) > 126));

class JavascriptMinify(object):

	def _outA(self):
		self.outstream.write(self.theA)
	def _outB(self):
		self.outstream.write(self.theB)

	def _get(self):
		"""return the next character from stdin. Watch out for lookahead. If
		   the character is a control character, translate it to a space or
		   linefeed.
		"""
		c = self.theLookahead
		self.theLookahead = None
		if c == None:
			c = self.instream.read(1)
		if c >= ' ' or c == '\n':
			return c
		if c == '': # EOF
			return '\000'
		if c == '\r':
			return '\n'
		return ' '

	def _peek(self):
		self.theLookahead = self._get()
		return self.theLookahead

	def _next(self):
		"""get the next character, excluding comments. peek() is used to see
		   if an unescaped '/' is followed by a '/' or '*'.
		"""
		c = self._get()
		if c == '/' and self.theA != '\\':
			p = self._peek()
			if p == '/':
				c = self._get()
				while c > '\n':
					c = self._get()
				return c
			if p == '*':
				c = self._get()
				while 1:
					c = self._get()
					if c == '*':
						if self._peek() == '/':
							self._get()
							return ' '
					if c == '\000':
						raise UnterminatedComment()

		return c

	def _action(self, action):
		"""do something! What you do is determined by the argument:
		   1   Output A. Copy B to A. Get the next B.
		   2   Copy B to A. Get the next B. (Delete A).
		   3   Get the next B. (Delete B).
		   action treats a string as a single character. Wow!
		   action recognizes a regular expression if it is preceded by ( or , or =.
		"""
		if action <= 1:
			self._outA()

		if action <= 2:
			self.theA = self.theB
			if self.theA == "'" or self.theA == '"':
				while 1:
					self._outA()
					self.theA = self._get()
					if self.theA == self.theB:
						break
					if self.theA <= '\n':
						raise UnterminatedStringLiteral()
					if self.theA == '\\':
						self._outA()
						self.theA = self._get()


		if action <= 3:
			self.theB = self._next()
			if self.theB == '/' and (self.theA == '(' or self.theA == ',' or
									 self.theA == '=' or self.theA == ':' or
									 self.theA == '[' or self.theA == '?' or
									 self.theA == '!' or self.theA == '&' or
									 self.theA == '|' or self.theA == ';' or
									 self.theA == '{' or self.theA == '}' or
									 self.theA == '\n'):
				self._outA()
				self._outB()
				while 1:
					self.theA = self._get()
					if self.theA == '/':
						break
					elif self.theA == '\\':
						self._outA()
						self.theA = self._get()
					elif self.theA <= '\n':
						raise UnterminatedRegularExpression()
					self._outA()
				self.theB = self._next()


	def _jsmin(self):
		"""Copy the input to the output, deleting the characters which are
		   insignificant to JavaScript. Comments will be removed. Tabs will be
		   replaced with spaces. Carriage returns will be replaced with linefeeds.
		   Most spaces and linefeeds will be removed.
		"""
		self.theA = '\n'
		self._action(3)

		while self.theA != '\000':
			if self.theA == ' ':
				if isAlphanum(self.theB):
					self._action(1)
				else:
					self._action(2)
			elif self.theA == '\n':
				if self.theB in ['{', '[', '(', '+', '-']:
					self._action(1)
				elif self.theB == ' ':
					self._action(3)
				else:
					if isAlphanum(self.theB):
						self._action(1)
					else:
						self._action(2)
			else:
				if self.theB == ' ':
					if isAlphanum(self.theA):
						self._action(1)
					else:
						self._action(3)
				elif self.theB == '\n':
					if self.theA in ['}', ']', ')', '+', '-', '"', '\'']:
						self._action(1)
					else:
						if isAlphanum(self.theA):
							self._action(1)
						else:
							self._action(3)
				else:
					self._action(1)

	def minify(self, instream, outstream):
		self.instream = instream
		self.outstream = outstream
		self.theA = '\n'
		self.theB = None
		self.theLookahead = None

		self._jsmin()
		self.instream.close()
