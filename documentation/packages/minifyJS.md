devWatchr minifyJS Package
=========================

Provides the **command** ``minifyJS`` to devWatchr.

Description
-----------

The ``minifyJS`` package allows you to combine all Javascript files from one directory into a single minified and single debug file.

It accepts these additional settings as well as the defaults:

**minify_to**

  The name of the file that you would like created in the watched directory for minified files. Ex: 'combined' will produce ``combined.min.js`` and ``combined.js``.
  
Prerequesites
-------------

None
  
Full settings.py Example
------------------------

```
  import pyinotify
  
  watch = [
  	{
    	'watch': '/home/ubuntu/myproject/js',
  		'handle': 'minifyJS',
  		'minify_to': 'combined',
  		'recursive': True,
  		'auto_add': True
  	}
  ]
```
