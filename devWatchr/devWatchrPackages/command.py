import pyinotify, subprocess, devWatchr

'''

'''

class command(devWatchr.watcher):
	def __init__(self, settings):
		self.settings = settings
		self.command = self.settings['command'].split()

	def _run(self,event):
		devWatchr.colors.printBlue('==> Running command %s' % self.settings['command'])
		if 'cwd' in self.settings:
			subprocess.Popen(self.command, cwd=self.settings['cwd'])
		else:
			subprocess.Popen(self.command)

handles = {
	'command': command
}
