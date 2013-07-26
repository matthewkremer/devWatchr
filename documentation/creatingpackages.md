Creating Custom Packages for devWatchr
======================================

Creating your own custom handles/packages for devWatchr is extremely simple. Each one is just a Python file with the following structure:

```
import devWatchr

class YOURHANDLEFUNCTION(devWatchr.watcher):
  
  def __init__(self, settings):
    self.settings = settings
  
  def _run(self, event):
    //YOUR CODE HERE
    
handles = {
  'YOURHANDLE': YOURHANDLEFUNCTION
}
```

You can have multiple handles per file, just add them to the handles dictionary and link them to their corresponding functions.

The settings directly from the devWatchr settings file will be passed to the ``__init__`` function and the event will be passed to your ``_run`` function.

The event Variable
------------------

The ``event`` object comes directly from pyinotify ([documentation here](http://pyinotify.sourceforge.net/#The_Event_Class)) and will have the following attributes:

wd (int): is the Watch Descriptor, it is an unique identifier who represents the watched item through which this event could be observed.

path (str): is the complete path of the watched item as given in parameter to the method .add_watch.

name (str): is not None only if the watched item is a directory, and if the current event has occurred against an element included in that directory.

mask (int): is a bitmask of events, it carries all the types of events watched on wd.

event_name (str): readable event name.

is_dir (bool): is a boolean flag set to True if the event has occurred against a directory.

cookie (int): is a unique identifier permitting to tie together two related 'moved to' and 'moved from' events.

Adding your Package to devWatchr
--------------------------------

After you have made your package, save the ``.py`` file to your ``devWatchrPackages`` folder (the example installation has this located at ``/usr/bin/devWatchrPackages``.

If you create a Package that you think would be useful to other developers, feel free to fork this repository and submit a pull request with your package added to ``devWatchr/devWatchr/devWatchrPackages`` and documentation added to ``devWatchr/documentation/packages/YOURPACKAGE.md``. For more information on how to submit a pull, visit [this tutorial](http://www.netmagazine.com/tutorials/share-your-open-source-project-github).
