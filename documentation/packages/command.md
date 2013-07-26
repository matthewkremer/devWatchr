devWatchr Command Package
=========================

Provides the **command** ``handle`` to devWatchr.

Description
-----------

The ``command`` package allows you to execute a system command.

It accepts two additional settings as well as the defaults:

**command**

  The actual command that you would like to run, ex: ``sudo supervisorctl restart all``.
  
**cwd**

  The working directory that you would like to execute the command in, ex: ``/home/user/myproject/``.
  
Prerequesites
-------------

None
  
Full settings.py Example
------------------------

```
  import pyinotify

  def check_ext(event):
    if not event.name[-3:] == ".py":
  		return False
  	return True
  
  watch = [
  	{
  		'watch': '/home/user/myproject',
  		'handle': 'command',
  		'command': 'sudo supervisorctl restart all',
      'cwd': '/home/user/myproject',
  		'check': check_ext,
  		'recursive': True,
  		'auto_add': True
  	}
  ]
```
