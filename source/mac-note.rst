********
Mac Note
********

:date: 2017-02-10
:modified: 2017-02-10
:slug: mac-note
:tags: mac, note
:category: software
:author: Dormouse Young
:summary: Note of how to use mac


Homebrew
========

date: 2017-02-05 22:34:28
modified: 2017-02-08 13:13:57

Office site: http://brew.sh/ .

Install
--------

Just Paste follow at a Terminal prompt::

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Usage
--------

Example::

    $ brew install wget

What is it?

Homebrew installs packages to their own directory and then symlinks their
files into ``/usr/local``::

    $ cd /usr/local
    $ find Cellar
    Cellar/wget/1.16.1
    Cellar/wget/1.16.1/bin/wget
    Cellar/wget/1.16.1/share/man/man1/wget.1

    $ ls -l bin
    bin/wget -> ../Cellar/wget/1.16.1/bin/wget

Homebrew-Cask
=============

Homebrew-Cask extends Homebrew and brings its elegance, simplicity, and
speed to the installation and management of GUI macOS applications such as
Google Chrome and Adium.

We do this by providing a friendly Homebrew-style CLI workflow for the
administration of macOS applications distributed as binaries.

It’s implemented as a homebrew external command called cask.

To start using Homebrew-Cask, you just need Homebrew installed.

Example::

    $ brew cask install atom
    ==> Satisfying dependencies
    complete
    ==> Downloading https://github.com/atom/atom/releases/download/v1.8.0/atom-mac.zip
    ######################################################################## 100.0%
    ==> Verifying checksum for Cask atom
    ==> Moving App 'Atom.app' to '/Applications/Atom.app'
    ==> Symlinking Binary 'apm' to '/usr/local/bin/apm'
    ==> Symlinking Binary 'atom.sh' to '/usr/local/bin/atom'
    🍺  atom was successfully installed!

And there we have it. Atom installed with one quick command: no clicking,
no dragging, no dropping.


Install firefox
===============

2017年 2月16日 星期四 21时48分05秒 CST

::

    wget -O FirefoxSetup.exe "https://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US"

    For other operating systems replace 'os=win' with:
       Windows 64bit              os=win64
       OS X                       os=osx
       Linux x86_64               os=linux64
       Linux i686                 os=linux

But it is very strange::

    MyMac:Downloads somebody$ wget -O FirefoxSetup.exe "https://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US"
    --2017-02-16 21:54:48--  https://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US
    Resolving download.mozilla.org... 54.149.16.117
    Connecting to download.mozilla.org|54.149.16.117|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: http://download.cdn.mozilla.net/pub/firefox/releases/51.0.1/mac/en-US/Firefox%2051.0.1.dmg [following]
    --2017-02-16 21:54:50--  http://download.cdn.mozilla.net/pub/firefox/releases/51.0.1/mac/en-US/Firefox%2051.0.1.dmg
    Resolving download.cdn.mozilla.net... 23.2.16.56, 23.2.16.64, 2402:4f00:4001::df77:3293, ...
    Connecting to download.cdn.mozilla.net|23.2.16.56|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 86166964 (82M) [application/x-iso9660-image]
    Saving to: ‘FirefoxSetup.exe’

    FirefoxSetup.exe               7%[==>                                           ]   6.46M   577KB/s    eta 1m 54s

So I have to go to http://ftp.mozilla.org/pub/firefox/releases/51.0.1/mac/en-US/ ,
and download manually.


bash
====

When login, mac will execute ``.bash_profile`` ，but not ``.bashrc``.
So we can add following to ``.bash_profile`` to run ``.bashrc`` ::

    if [ -f ~/.bashrc ]; then
       source ~/.bashrc
    fi


Install wxpython
================

::

    brew install wxmac
    brew install wxpython


Install cTags
=============

If you use the cTags directly on Mac will result following errors::

    ctags: illegal option -- R
    usage: ctags [-BFadtuwvx] [-f tagsfile] file ...错误。

Beacuse the Mac's own cTags does not support the ``-R`` parameter.
So we should install cTags by ourself::

    brew install ctags

After install cTags, if still have errors, we should check ``$PATH``::

    $ $PATH

We can find ``/usr/local/bin`` is not in the ``$PATH``. We have way to add
it.

Way one:

Delete Mac's ctags::

    sudo rm /usr/bin/ctags

Create a soft link::

    sudo ln -s /usr/local/Cellar/ctags/5.8_1/bin/ctags /usr/bin/ctags

Way two:

Edit ``~/.bash_profile``, add following line::

    export PATH=/usr/local/bin:$PATH

I recommend the second way for most of brew intalled software are in the
``/usr/local``.


Some software
=============

video covert: handbrake(https://handbrake.fr)
