==================
Python GTK+ 3 笔记
==================
:date: 2015年 06月 27日 星期六 16:03:07 CST
:author: Dormouse.Young(dormouse.young@gmail.com)

本文基于 Linux Mint 17 Cinnamon 64-bit, Python 2.7.6, PyGObject 3.12.0 。

安装
====

Python GTK+ 3 编程现在推荐使用 PyGObject。

Python GTK+ 2 编程现在推荐使用 PyGTK。

其依赖于：

* GTK+3
* Python 2 (2.6 or later) or Python 3 (3.1 or later)
* gobject-introspection

安装方法见其主页： https://wiki.gnome.org/Projects/PyGObject


Hello World
===========

.. literalinclude:: hello.py


信号
====

::

    handler_id = widget.connect("event", callback, data)
    widget.disconnect(handler_id)


控件属性
========

以下两种方式是等价的::

    label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)

    label = Gtk.Label()
    label.set_label("Hello World")
    label.set_angle(25)
    label.set_halign(Gtk.Align.END)

还可以使用以下方式::

    widget.get_property("prop-name")
    widget.set_property("prop-name", value),

查看控件属性的方式::

    widget = Gtk.Box()
    print(dir(widget.props))


Unicode
=======

GTK+ 内部使用 UTF-8。 PyGObject 会自动把 unicode 参数转换为 UTF-8 。
示例::

    >>> from gi.repository import Gtk
    >>> unicode_string = u"中国"
    >>> label = Gtk.Label()
    >>> label.set_text(unicode_string)
    >>> txt = label.get_text()
    >>> type(txt), txt
    (<type 'str'>, '\xe4\xb8\xad\xe5\x9b\xbd')
    >>> txt == unicode_string
    __main__:1: UnicodeWarning: Unicode equal comparison failed to convert
    both arguments to Unicode - interpreting them as being unequal
    False
    >>> txt.decode("utf-8")
    u'\u4e2d\u56fd'
    >>> txt.decode("utf-8")==unicode_string
    True

容器
====

单儿子容器是 Gtk.Bin 的后代，多儿子容器是 Gtk.Container 的后代。

常用容器为 boxes (Gtk.Box) 、 tables (Gtk.Table) 和 (Gtk.Grid) 。

Box
---

Box 的组装函数为 Gtk.Box.pack_start() 或 Gtk.Box.pack_end() 。

.. literalinclude:: box.py
