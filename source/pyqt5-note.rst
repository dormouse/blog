PyQt5 Note
==========


:date: 2017-05-15
:modified: 2017-05-15
:slug: pyqt5-note
:tags: pyqt, note
:category: development
:author: Dormouse Young
:summary: Note of PyQt5

安装 PyQt5 及其文档
--------------------

unbuntu::

    sudo apt-get install python3-pyqt5 pyqt5-doc pyqt5-examples
    sudo apt-get install qtbase5-doc

示例所在目录：/usr/share/doc/pyqt5-examples/examples/qtdemo/qtdemo.py

Qt5 文档所在目录： /usr/share/qt5/doc

安装更多::

    sudo apt-get install python3-pyqt5* qtbase5-doc
    sudo apt-get install qt5-doc qttools5-dev-tools

OSX::

    brew install python3

    Pip, setuptools, and wheel have been installed. To update them
      pip3 install --upgrade pip setuptools wheel

    You can install Python packages with
      pip3 install <package>

    They will install into the site-package directory
      /usr/local/lib/python3.6/site-packages

    See: http://docs.brew.sh/Homebrew-and-Python.html

    brew install pyqt5

文档和示例都在源代码中，下载：https://sourceforge.net/projects/pyqt/files/PyQt5/

assistant : /usr/local/Cellar/qt/5.9.0/libexec/Assistant.app
/usr/local/Cellar/qt5/5.6.1-1/libexec/Assistant-qt5.app/Contents/MacOS/Assistant

PyCharm 配置相关工具
--------------------

Linux Mint

qt5desinger::

    Program: /usr/lib/x86_64-linux-gnu/qt5/bin/designer
    Parameters: $FileName$
    Working directory: $FileDir$

pyuic::

    Program: python3
    Parameters: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutAllExtensions$_ui.py
    Working directory: $FileDir$

qt5assistant::

    Program: /usr/lib/x86_64-linux-gnu/qt5/bin/assistant

关于 model index
-----------------

获得 model index::

    index = model.index(row, column, QModelIndex())

设置 model 的值::

    model.setData(index, value, Qt.EditRole)

Some tips
---------

widget connect signal with parameter::

    self.button1.clicked.connect(lambda : do_stuff('btn one'))
    self.button2.clicked.connect(lambda : do_stuff('btn two'))

move window to center of screen::

    self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())

TreeView
--------

set columnt width::

    view->header()->setStretchLastSection(false);
    view->header()->setResizeMode(INDEX_COLUMN_SKU, QHeaderView::Interactive);
    view->header()->setResizeMode(INDEX_COLUMN_NAME, QHeaderView::Stretch);
    view->header()->setResizeMode(INDEX_COLUMN_QUANTITY, QHeaderView::Interactive);
    view->header()->setResizeMode(INDEX_COLUMN_PRICE, QHeaderView::Interactive);
