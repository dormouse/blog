Tinkerer Quick Start
********************

:date: 2017-02-01
:slug: tinkerer-quick-start
:tags: tinkerer, blog
:category: software
:author: Dormouse Young
:summary: Tinkerer is a Python blogging engine/static website generator
          powered by Sphinx.

Install
=======
::

    $ sudo pip install tinkerer


Quick start
===========
::

    $ mkdir tinkerer_blog
    $ cd tinkerer_blog
    $ tinker --setup

Then edit the ``conf.py``.


Tip
===
- Add post: ``tinker --post 'Hello World!'``
- Add page: ``tinker --page 'About'``
- Build blog: ``tinker --build``


Todo
====
- Show local toc in sidebar


Reference
=========
Tinkerer Homepage: http://tinkerer.me/index.html
