devWatchr Documentation
=======================

devWatchr allows you to watch files or folders for changes and then immediately invoke an operation during development. For instance, when you save a Javascript file, you could automatically minify all of your javascript files into a single minified file using the minifyJS package.

It's extremely easy to add your own packages and you can set up an individual "settings" file for each of your projects.

If you create a Package that you think would be useful to other developers, feel free to fork this repository and submit a pull request with your package added to devWatchr/devWatchr/devWatchrPackages and documentation added to devWatchr/documentation/packages/YOURPACKAGE.md.

General Documentation
---------------------

[How to Use](https://github.com/matthewkremer/devWatchr/blob/master/documentation/howtouse.md)

[How to Create Your own Packages](https://github.com/matthewkremer/devWatchr/blob/master/documentation/creatingpackages.md)

Packages
--------

[command](https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/command.md): Allows you to execute a command line operation.

[compass](https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/compass.md): Allows you to compile SASS or SCSS.

[minifyJS](https://github.com/matthewkremer/devWatchr/blob/master/documentation/packages/minifyJS.md): Allows you to minify a folder of Javascript files. Also provides a debug version of the combined scripts.
