*************************************
如何创建 Sublime Text 3 插件
*************************************

:date: 2017-11-07
:modified: 2017-11-07
:slug: howto-create-a-sublime-text-3-plugin
:tags: sublime, plugin
:category: software
:author: Dormouse Young

本文的测试环境为:

* Linux Mint 18.2 'Sonya'
* Sublime Text Version 3.0, Build 3143
* Python 3.6.2 ``|Anaconda, Inc.|`` (default, Sep 22 2017, 02:03:08) [GCC 7.2.0] on linux

第一个插件
==========

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

参考：

* https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685
* http://sublimetext.info/docs/en/extensibility/plugins.html
