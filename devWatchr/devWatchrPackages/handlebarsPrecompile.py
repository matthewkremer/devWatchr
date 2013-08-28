import pyinotify, os, os.path, subprocess, devWatchr
from StringIO import StringIO

'''
	View Documentation here:
	https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/handlebarsPrecompile.md
'''

class precompile(devWatchr.watcher):
	def __init__(self, settings):
		self.settings = settings
		if 'recursive' not in self.settings:
			self.settings['recursive'] = False

	def _run(self,event):
		if not event.name[-11:] == ".handlebars":
		  return
		  
		devWatchr.colors.printBlue('==> Handlebars Modification Detected')
		
		compile_path = self.settings['watch']
		compile_to = self.settings['compile_to']
		
		command = ('sudo handlebars %s -f %s.js -o -m' % (compile_path, compile_to)).split()
		
		if 'cwd' in self.settings:
		  subprocess.Popen(command, cwd=self.settings['cwd'])
		else:
			subprocess.Popen(command)
  
		devWatchr.colors.printGreen('Compiled Handlebars: %s.js' % compile_to)

handles = {
	'handlebarsPrecompile': precompile
}
