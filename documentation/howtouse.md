Setting up DevWatchr
====================

In order to set up devWatchr you will need to create a settings python file corresponding to your project.

This is what your settings file should look like:

```
  import pyinotify
  
  watch = [
    {
      'watch': '/this/is/the/folder/were/watching',
      'handle': 'The handle of a package'
    }
  ]
  
```

``watch`` should be a list of python dictionaries that have at least ``watch`` and ``handle`` included.

Each package will have at least one ``handle`` assocated with it that you can use to link a watch to it.

There are several defaulted options that are available to you for every package:

**recursive**

  Defaults to False. Set to True if you want the watch to include all subdirectories.
  
**auto_add**

  Defaults to False. Set to True if you want a recursively watched directory to also watch directories that are added while the script is running.
  
**do_glob**

  Defaults to False. Expands paths expressions and includes them as watched paths, see the [glob module](http://docs.python.org/library/glob.html) for more details.
  
**check**

  Configuring a "check" for a watch means that you would like to check something before the script is actually executed. For instance, if you want to restart your web server when a ``.py`` file is changed in a directory, you may want to first check whether or not the edited file in that directory was indeed a ``.py`` file like so:
  
  ```
    import pyinotify

    def check_ext(event):
      if not event.name[-3:] == ".py":
    		return False
    	return True
    
    watch = [
    	{
    		'watch': '/home/ubuntu/myproject',
    		'handle': 'command',
    		'command': 'sudo supervisorctl restart all',
    		'check': check_ext,
    		'recursive': True,
    		'auto_add': True
    	}
    ]
  ```
