*****************
Sublime Text Note
*****************

:date: 2017-01-19 12:48:01
:modified: 2017-09-25
:slug: sublime-text-note
:tags: sublime, note, plugin
:category: software
:author: Dormouse Young
:summary: Note for sublime text.
          Sublime Text is a sophisticated text editor for code, markup and prose.
          You'll love the slick user interface, extraordinary features and amazing
          performance.


Install Sublime Text3
=====================

Install the GPG key::

    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

Ensure apt is set up to work with https sources::

    sudo apt-get install apt-transport-https

Select the channel to use:

Stable::

    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

Dev::

    echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

Update apt sources and install Sublime Text::

    sudo apt-get update
    sudo apt-get install sublime-text


Install Package Control
=======================

在 sublime text3 的终端中运行如下代码安装 Package Control ，终端打开方法为
使用 ``ctrl + ``` 快捷键或者选择菜单 ``View > Show Console`` ::

    import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)



.. attention::
    以上代码全因为 Sublime Text 的版本不同而变化，
    请到 https://packagecontrol.io/installation 复制最新的代码。

通过 ``ctrl+shift+p`` 进入 ``Command Palette`` ，输入
``Package Contorl: Install Package`` (简写为 ``ip`` )，回车执行，
进入插件的搜索窗口，查找选择到需要的插件后，回车即可进行安装，
安装状态在最下面的状态栏内会有文字提示。

See `offical docs <https://packagecontrol.io/docs>`_ for detail.


Install Packages
================

Packages will install in ``~/.config/sublime-text-3/Installed Packages/somename.sublime-package``.
"somename.sublime-package" is a zipfile,
you can overwrite the contents in the zipfile by put same name file in
``~/.config/sublime-text-3/Packages/somename``.


Anaconda
----------------

Usage: http://damnwidget.github.io/anaconda/IDE/


GraphvizPreview
-----------------

GraphvizPreview Plugin can not preview in my PC, my env is:

* Linux Mint 18.2 'Sonya'
* Sublime Text Version 3.0, Build 3143
* Python 3.6.2 ``|Anaconda, Inc.|`` (default, Sep 22 2017, 02:03:08) [GCC 7.2.0] on linux

The output is ::

    (xreader:8971): Gtk-ERROR **: GTK+ 2.x symbols detected.
    Using GTK+ 2.x and GTK+ 3 in the same process is not supported

GraphvizPreview first covert code to pdf format, then use ``xdg-open`` to
open the output file. So hack it, first covert code to png format, then use
``feh`` to open it.

There is my modifyed GraphvizPreview:

.. literalinclude:: GraphvizPreview.py
   :language: Python


Play with evernote
-------------------

Use Sublime Text plugin for Evernote, you and read and write evernote.

This package is based on SublimeEvernote for ST2 but is only supported on
ST3 and adds many new features.

To start using it install it from Package Control and type "Evernote" on
the Command Palette (``ctrl+shift+p``).
See `First Use <https://github.com/bordaigorl/sublime-evernote#first-use>`_
for linking the plugin to your account.



Use Fcitx in Sublime Text 3
===========================

Sublime text 3 is not support fcitx, so patch it::

    $ wget https://github.com/yuan3y/sublime_zh_patch/archive/patch-1.zip
    $ unzip patch-1.zip
    $ cd sublime_zh_patch-patch-1/
    $ sudo ./setup.sh
    $ sudo apt-get install fcitx fcitx-config-gtk fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-table-wubi


My Settings
===========

Flowing is my settings::

    {
        "auto_complete": false,
        "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
        "ensure_newline_at_eof_on_save": true,
        "file_exclude_patterns":[
            ".DS_Store",
            "*.pid",
            "*.pyc"
        ],
        "find_selected_text": true,
        "fold_buttons": false,
        "folder_exclude_patterns":[
            ".git",
            "__pycache__"
        ],
        "font_face": "ubuntu mono",
        // for OSX
        // "font_face": "PT Mono",
        "font_size": 12.0,
        "font_options":
        [
            "subpixel_antialias",
            "no_bold"
        ],
        "highlight_line": true,
        "ignored_packages": [],
        "line_padding_bottom": 1,
        "line_padding_top": 1,
        "rulers": [75, 80],
        "scroll_past_end": false,
        "show_full_path": true,
        "show_minimap": false,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true
    }


如何创建 Sublime Text 3 插件
========================================

:date: 2017-11-07
:modified: 2017-11-07

本文的测试环境为:

* Linux Mint 18.2 'Sonya'
* Sublime Text Version 3.0, Build 3143
* Python 3.6.2 ``|Anaconda, Inc.|`` (default, Sep 22 2017, 02:03:08) [GCC 7.2.0] on linux

第一个插件
----------------------

在菜单中选择 ``Tools -> Deveolper -> New Plugin...`` 。
Sublime Text 会新建一个文件，内容如下::

    import sublime
    import sublime_plugin


    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")

保存这个文件，文件名为 ``hello.py`` 。缺省的保存目录为
``~/.config/sublime-text-3/Packages/User/`` 。

打开 Sublime Text 终端（快捷键： ``Ctrl+```），输入命令
``view.run_command('example')`` ，你会发现当前文件的开头插入了
``Hello, World!`` 。

如果你是一个 Python 程序员，那么你可以轻松的解理 Sublime Text 的插件本质是一个
Python 程序。如果你不是一个 Python 程序员，那么现在开始学习 Python 是一个不错
的主意。

这个程序首先导入了 ``sublime`` 和 ``sublime_plugin`` 两个模块，
然后定义了一个 ``sublime_plugin.TextCommand`` 的子类，其 ``run`` 方法中内容就
是插件运行的入口。

这里要注意的是我们在终端中运行的名称是 ``example`` 而不是 ``ExampleCommand`` ，
这是 Sublime Text 自身的命名约定。这个约定是：首先去掉后缀 ``Command`` ，然后
把名称由驼峰式（ CamelCaseinto ）转化为下划线式 （ underscore_notation ）。
例如你的类的名称如果是 ``DormouseFirstPlugin`` 那么就会转化为
``my_first_plugin`` 。


Ref
===

- https://www.zhihu.com/question/33409254
- Sublime Text Document: `Linux Package Manager Repositories <https://www.sublimetext.com/docs/3/linux_repositories.html>`_

- https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685
- http://sublimetext.info/docs/en/extensibility/plugins.html
