Installing devWatchr
====================

Prerequisites
-------------

You must have Python and [pyinotifiy](http://pyinotify.sourceforge.net/) installed on your system.

Installation
------------

To install devWatchr on your linux system, you must pull the contents of the ``devWatchr/devWatchr`` folder into somewhere that is available on your system path (I used ``/usr/bin/``).

You can download a zip of the entire project [here](https://github.com/matthewkremer/devWatchr/archive/master.zip)
and move the contents of the ``devWatchr/devWatchr`` folder over to your server manually or ``git clone`` and ``cp`` it using a command like below. You must also add executable permissinos to ``devWatchr.py``.

```
  git clone git@github.com:matthewkremer/devWatchr devWatchr
  sudo cp -r devWatchr/devWatchr/* /usr/bin/
  sudo chmod +x /usr/bin/devWatchr.py
```

The structure you want to end up with is:

```
  /usr
    /bin
      devWatchr.py
      /devWatchrPackages
        __init__.py
        Packages .py Files Here
```
