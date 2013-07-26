devWatchr Compass Package
=========================

Provides the **compassCompile** ``handle`` to devWatchr.

Description
-----------

The ``compass`` package allows you to compile SASS/SCSS code using Compass.

It accepts these additional settings as well as the defaults:
  
**cwd**

  The working directory that you would like to execute the command in, ex: ``/home/user/myproject/src``. This will be prepended to all Compass settings from below.
  
**--css-dir**

  The directory that you would like the compiled css to go in.
  
**--sass-dir**

  The directory that contains your non-compiled SASS or SCSS scripts.
  
**--images-dir**

  The directory that contains your non-compiled images for use by compass.
  
**--output-style**

  The output style from Compass settings that you would like to use.
  
**--no-line-comments**

  Set to ``True`` to remove line comments from your compiled CSS.
  
**Additonal Compass Settings**

  For more information about Compass settings please visit [this page](http://compass-style.org/help/tutorials/configuration-reference/). You can use any arguments that you would normally pass to the compass command line.
  
Prerequesites
-------------

You must install ``Ruby`` and the Compass Command Line Tool on your system.

[Installing Ruby](http://www.ruby-lang.org/en/downloads/)

[Installing Compass Command Line Tool](http://compass-style.org/install/)
  
Full settings.py Example
------------------------

```
  import pyinotify
  
  watch = [
  	{
    	'watch': '/home/ubuntu/myproject/scss',
  		'handle': 'compassCompile',
  		'--css-dir': 'css',
  		'--sass-dir': 'scss',
  		'--images-dir': 'images',
  		'--output-style': 'compressed',
  		'--no-line-comments': True,
  		'cwd': '/home/ubuntu/myproject/'
  	}
  ]
```

Questions & Issues
------------------

If you have an issue or question about devWatchr, please open a Github issue on our [issues page](https://github.com/matthewkremer/devWatchr/issues).
