alternativez [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
[![PyPi Status](https://img.shields.io/pypi/v/alternativez.svg)](https://pypi.python.org/pypi/alternativez)
[![TravisCI Build Status](https://travis-ci.org/KOLANICH/alternativez.py.svg?branch=master)](https://travis-ci.org/KOLANICH/alternativez.py)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/alternativez.py.svg)](https://coveralls.io/r/KOLANICH/alternativez.py)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/alternativez.py.svg)](https://libraries.io/github/KOLANICH/alternativez.py)

A tool helping managing alternatives: packages with compatible API doing the same thing, but having different IDs. The name is inspired with [Debian alternatives](https://wiki.debian.org/DebianAlternatives). They may be different forks of one package, or completely independent packages having functions with the same API and doing the same things because it was an obvious solution. This library allows you not strictly require them all, but any of them, and it also allows to import them into your app in an easy way.

Requirements
------------
* [```Python 3```](https://www.python.org/downloads/). [```Python 2``` is dead, stop raping its corpse.](https://python3statement.org/) Use ```2to3``` with manual postprocessing to migrate incompatible code to ```3```. It shouldn't take so much time.
