import pyinotify, subprocess, devWatchr

'''
	Compiles SASS/SCSS using Compass. Settings include the default settings and:
	{
		'cwd': The current working directory that should be used when running the compass command.
		Any available Compass commands that can be sent.
		Ex:
		'--css-dir': '/home/user/myproject/css/'
		Any Compass command that do not need a corresponding value should have their value set to True.
		Ex:
		'--no-line-comments': True
	}
'''

class compassCompile(devWatchr.watcher):
	def __init__(self, settings):
		self.settings = settings
		self.compile_str = 'compass compile'
		for key, value in settings.iteritems():
			if key[0:1] == "-":
				if value == True:
					self.compile_str = '%s %s' % (self.compile_str, key)
				else:
					self.compile_str = '%s %s=%s' % (self.compile_str, key, value)
		self.compile_str = self.compile_str.split()

	def _run(self, event):
		if event.name[-5:] != ".scss" and event.name[-5:] != ".sass":
			return
		devWatchr.colors.printBlue('==> Compass CSS Modification Detected')
		if 'cwd' in self.settings:
			subprocess.Popen(self.compile_str, cwd=self.settings['cwd'])
		else:
			subprocess.Popen(self.compile_str)

handles = {
	'compassCompile': compassCompile
}
