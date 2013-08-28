#!/usr/bin/env python

"""
        devWatchr is complete open source, just be sure to leave this disclaimer and text in.
        Use it for good, not evil!
        
        Documentation and information can be found at http://devwatchr.com/
        
        Made by Matthew Kremer in 2013:
        https://github.com/matthewkremer
        http://www.linkedin.com/in/matthewkremer

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
        IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
        FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
        CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
        DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF 
        USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
        WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN 
        ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import imp, os, sys, os.path, pyinotify, getopt, devWatchrPackages

class watcher(pyinotify.ProcessEvent):
        def _run_cmd(self,event):
                if 'check' in self.settings:
                        if not self.settings['check'](event):
                                return
                self._run(event)
        def process_IN_ACCESS(self, event):
                self._run_cmd(event)
        def process_IN_ATTRIB(self, event):
                self._run_cmd(event)
        def process_IN_CLOSE_NOWRITE(self, event):
                self._run_cmd(event)
        def process_IN_CLOSE_WRITE(self, event):
                self._run_cmd(event)
        def process_IN_CREATE(self, event):
                self._run_cmd(event)
        def process_IN_DELETE(self, event):
                self._run_cmd(event)
        def process_IN_DELETE_SELF(self, event):
                self._run_cmd(event)
        def process_IN_IGNORED(self, event):
                self._run_cmd(event)
        def process_IN_MODIFY(self, event):
                self._run_cmd(event)
        def process_IN_MOVE_SELF(self, event):
                self._run_cmd(event)
        def process_IN_MOVED_FROM(self, event):
                self._run_cmd(event)
        def process_IN_MOVED_TO(self, event):
                self._run_cmd(event)
        def process_IN_OPEN(self, event):
                self._run_cmd(event)
        def process_IN_Q_OVERFLOW(self, event):
                self._run_cmd(event)
        def process_IN_UNMOUNT(self, event):
                self._run_cmd(event)
                
class multiWatcher(watcher):
        def __init__(self, settings):
		self.settings = settings
		self.handlers = self.settings['handle'].split('|')

	def _run(self,event):
		for handler in self.handlers:
		        tempWatcher = handlers[handler](self.settings)
		        tempWatcher._run(event)
		
class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

        def printBlue(self,s):
                print bcolors.OKBLUE + s + bcolors.ENDC

        def printGreen(self,s):
                print bcolors.OKGREEN + s + bcolors.ENDC

        def printWarning(self,s):
                print bcolors.WARNING + s + bcolors.ENDC

        def printFail(self,s):
                print bcolors.FAIL + s + bcolors.ENDC

        def printHeader(self,s):
                print bcolors.HEADER + s + bcolors.ENDC

colors = bcolors()

def help():
        colors.printFail('You must execute devWatchr with the path to a settings python file.')
        colors.printFail('Ex: devWatchr /home/usr/devWatchrSettings.py')
        colors.printFail('Visit www.devwatchr.com for more information')
        sys.exit()

if __name__ == '__main__':
        availablePackages = devWatchrPackages.__all__
        handlers = {}

        defaults = {
                'recursive': False,
                'auto_add': False,
                'do_glob': False,
                'events': pyinotify.IN_CLOSE_WRITE|pyinotify.IN_CREATE|pyinotify.IN_DELETE
        }

        for p in availablePackages:
                if not p[0:2] == "__":
                        f = __import__('devWatchrPackages.%s' % p, globals(), locals(),['*'])
                        for key,value in f.handles.iteritems():
                                handlers[key] = value
        if len(sys.argv) == 2:
                config = sys.argv[1]
                config = imp.load_source('config', config)
        else:
                help()

        print bcolors.HEADER + 'devWatchr has started.' + bcolors.ENDC

        wm = pyinotify.WatchManager()
        for w in config.watch:
                watch = {}
                watch.update(defaults)
                watch.update(w)
                if '|' in watch['handle']:
                        wm.add_watch(watch['watch'],watch['events'],multiWatcher(watch),watch['recursive'],watch['auto_add'],watch['do_glob'])
                else:
                        wm.add_watch(watch['watch'],watch['events'],handlers[watch['handle']](watch),watch['recursive'],watch['auto_add'],watch['do_glob'])
                print bcolors.OKGREEN + ('Watching %s with %s.' % (watch['watch'],watch['handle'])) + bcolors.ENDC
        notifier = pyinotify.Notifier(wm)
        notifier.loop()

