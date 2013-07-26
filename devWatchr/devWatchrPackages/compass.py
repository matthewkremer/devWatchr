import pyinotify, subprocess, devWatchr

'''
	View Documentation here:
	https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/compass.md
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
