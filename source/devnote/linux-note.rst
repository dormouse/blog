**************
Linux Note
**************

:date: 2016-05-27
:modified: 2017-09-25
:slug: linux-note
:tags: linux, note
:category: software
:author: Dormouse Young
:summary: Note of how to use linux

Pip note
==========

Install with pip: ``pip install imapclient``.

Install from source::

    $ git clone https://github.com/mjs/imapclient.git
    $ cd imapclient
    $ pip install -e .

Show package inof: ``pip show package-name`` , for example::

    $ pip show PyQt5
    Name: PyQt5
    Version: 5.15.4
    Summary: Python bindings for the Qt cross platform application toolkit
    Home-page: https://www.riverbankcomputing.com/software/pyqt/
    Author: Riverbank Computing Limited
    Author-email: info@riverbankcomputing.com
    License: GPL v3
    Location: /home/user-name/anaconda3/envs/jtjd/lib/python3.9/site-packages
    Requires: PyQt5-Qt5, PyQt5-sip


Install chrome
==================

date: 2016-05-27

::

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo gdebi google-chrome-stable_current_amd64.deb

Install new font
=====================

date: 2015-04-29

How-to:

For system wide installation, copy the fonts to ``/usr/share/fonts`` and run
``sudo fc-cache`` to rebuild the font cache, or for user local installation,
make sure ``~/.fonts`` exists, copy them into there, then rebuild the font
cache.

Example:

Install `adobe-fonts/source-code-pro
<https://github.com/adobe-fonts/source-code-pro>`_ in Ubuntu 14.04::

    [ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
    sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
    sudo fc-cache -f -v


Install Downlaod tools
=========================

Date: 2017-07-12

Install uGet::

    sudo add-apt-repository ppa:plushuang-tw/uget-stable
    sudo apt update
    sudo apt install uget

Install aria2::

    sudo apt-get install aria2

Install firefox plugin FlashGot


以交互模式查找历史命令
=================================

用 ``history`` 可以查找历史命令。

在终端可以使用 ``Ctrl + r`` 命令搜索历史命令。使用方法是先按下
``Ctrl + r`` ，然后输入字符就会显示包含字符的历史命令。再次按下
``Ctrl + r`` 会向后搜索更老的命令，或者按下 ctrl+s 向前搜索。

注意，``Ctrl + s`` 有时会与 ``XON/XOFF`` 流控制冲突，即 ``XON/XOFF`` 流控
制也会使用该快捷键。你可以通过运行 stty -ixon 命令来禁用该快捷键。在你的个
人电脑上，这通常是有用的，但是在禁用前，确保你不需要 XON/XOFF 。


使用 at 命令
=================================

``at`` 命令的运行方式是在后面紧跟着你想要运行任务的运行时间。时间是灵活
的，因为它支持许多时间格式。包括下面这些例子::

    at 12:00 PM September 30 2017
    at now + 1 hour
    at 9:00 AM tomorrow

当你以带参数的方式输入 `at` 命令以后，将会提示你该命令将在你的 Linux 系统
上运行。这可能是一个备份脚本，一套维护任务，或者甚至是一个普通的 bash
命令。如果要结束任务，可以按 ctrl+d 。

另外，你可以使用 `atq` 命令查看当前用户的所有任务，或者使用 `sudo atq`
查看所有用户的任务。它将会展示出所有排定好的任务，并且每个任务都伴有一个
ID 。如果你想取消一个排定好的任务，可以使用 `atrm` 命令，并且以任务 ID
作为参数。

通过子 shell 保持当前目录
=================================

通过子 shell 可以在当前目录执行其他目录下的内容。子 shell 是一个包含在括号
中的命令，例如：``(cd /etc && ls -a)`` 。这个命令会输出 ``/etc`` 中的内容，
并且保持当前目录不变。

其工作原理是：一个括号中的命令会创建一个子 shell 或当前 shell 的副本。
该子 shell 可以访问所有的父变量，反之则不行。所以请记住，你是在运行一个
非常复杂的单行命令。

用 shred 命令更安全地删除文件
=================================

使用 shred 命令删除一个文件之后，文件中的数据会被多次随机覆写。甚至有一个
选项可以在随机覆写之后对所有的数据进行清零。

如果你想安全的删除一个文件并且以零覆盖，那么可以使用下面的命令::

    shred -u -z [file name]

同时，你也可以使用 -n 选项和一个数字作为参数，从而指定在随机覆盖数据的时候
迭代多少次。


你可以按照功能搜索命令，而不仅仅是通过名字
========================================================

记住命令的名字非常困难，特别是对于初学者来说。幸运的是，Linux 附带了一个
通过名字和描述来搜索 man 页面的工具。

下次，如果你没有记住你想要使用的工具的名称，你可以尝试使用 apropos 命令
加上你想要干的事情的描述。比如，apropos build filesystem 将会返回一系列
名字和描述包括了 “build” 和 “filesystem” 单词的工具。

apropos 命令接受一个或多个字符串作为参数，但同时它也有其他参数，比如你可以
使用 -r 参数，从而通过正则表达式来搜索。

一个允许你来管理系统版本的替代系统
========================================================

如果你曾进行过软件开发，你就会明白跨项目管理不同版本的语言的支持的重要性。
许多 Linux 发行版都有工具可以来处理不同的内建版本。

可执行文件比如 java 往往符号链接到目录 /etc/alternatives 下。反过来，该
目录会将符号链接存储为二进制文件并提供一个管理这些链接的接口。Java 可能是
替代系统最常管理的语言，但是，经过一些配置，它也可以作为其他应用程序替代
品，比如 NVM 和 RVM （NVM 和 RVM 分别是 NodeJS 和 Ruby 的版本管理器）。

在基于 Debian 的系统中，你可以使用 update-alternatives 命令创建和管理这些
链接。在 CentOS 中，这个工具就叫做 alternatives 。通过更改你的 alternatives
文件中的链接，你便可以安装一个语言的多个版本，并且在不同的情况下使用不同的
二进制。这个替代系统也提供了对任何你可能在命令行运行的程序的支持。

通过自动更正来避免输入很长的无效文件路径
========================================================

有多少次，你输入一个文件的绝对路径，然而却看到“没有该文件或目录”的消息。
任何人都会明白输入一个很长的字符串的痛苦。幸运的是，有一个很简单的解决办法。

内建的 shopt 命令允许你设置不同的选项来改变 shell 的行为。设置 cdspell 选项
是避免输入文件路径时一个字母出错的头痛的一个简单方式。你可以通过运行
``shopt -s cdspell`` 命令来启用该选项。启用该选项后，当你想要切换目录时，会
自动更正为最匹配的目录。

Shell 选项是节省时间的一个好方法（更不用说减少麻烦），此外还有许许多多的
其他选项。如果想查看你的系统中所有选项的完整列表，可以运行不带参数的 shopt
命令。需要注意的是，这是 bash 的特性，如果你运行 zsh 或者其他可供选择的
shell，可能无法使用。

压缩和解压缩
==================

常用命令
--------

+----------+---------------------------+---------------------------------------+
| 扩展名   | 解压                      | 打包                                  |
+==========+===========================+=======================================+
| .tar     | tar xvf FileName.tar      | tar cvf FileName.tar DirName          |
+----------+---------------------------+---------------------------------------+
| .tar.gz  | tar zxvf FileName.tar.gz  | tar zcvf FileName.tar.gz DirName      |
+----------+---------------------------+---------------------------------------+
| .tar.bz2 | tar jxvf FileName.tar.bz2 | tar jcvf FileName.tar.bz2 DirName     |
+----------+---------------------------+---------------------------------------+
| .gz      | gunzip FileName.gz        | gzip FileName                         |
|          | gzip -d FileName.gz       |                                       |
+----------+---------------------------+---------------------------------------+
| .bz2     | bzip2 -d FileName.bz2     | bzip2 -z FileName                     |
|          | bunzip2 FileName.bz2      |                                       |
+----------+---------------------------+---------------------------------------+
| .bz      | bzip2 -d FileName.bz      |                                       |
|          | bunzip2 FileName.bz       |                                       |
+----------+---------------------------+---------------------------------------+
| .tar.bz  | tar jxvf FileName.tar.bz  |                                       |
+----------+---------------------------+---------------------------------------+
| .Z       | uncompress FileName.Z     | compress FileName                     |
+----------+---------------------------+---------------------------------------+
| .tar.Z   | tar Zxvf FileName.tar.Z   | tar Zcvf FileName.tar.Z DirName       |
+----------+---------------------------+---------------------------------------+
| .tgz     | tar zxvf FileName.tgz     |                                       |
+----------+---------------------------+---------------------------------------+
| .tar.tgz | tar zxvf FileName.tar.tgz | tar zcvf FileName.tar.tgz FileName    |
+----------+---------------------------+---------------------------------------+
| .zip     | unzip FileName.zip        | zip FileName.zip DirName              |
+----------+---------------------------+---------------------------------------+
| .rar     | rar a FileName.rar        | rar e FileName.rar                    |
+----------+---------------------------+---------------------------------------+
| .lha     | lha -e FileName.lha       | lha -a FileName.lha FileName          |
+----------+---------------------------+---------------------------------------+

sEx
---

.tar .tgz .tar.gz .tar.Z .tar.bz .tar.bz2 .zip

.cpio .rpm .deb .slp .arj .rar .ace .lha .lzh

.lzx .lzs .arc .sda .sfx .lnx .zoo .cab .kar .

cpt .pit .sit .sea

解压::

    sEx x FileName.*

压缩::

    sEx a FileName.* FileName

sEx只是调用相关程序，本身并无压缩、解压功能，请注意！

分卷压缩及解压分卷压缩文件
------------------------------------------------

使用rar

1.分卷压缩

ubuntu下没有默认安装rar，可以通过 sudo apt-get install rar,sudo apt-get install unrar 来安装rar.

安装过后，使用以下命令进行分卷压缩::

    rar a -vSIZE  压缩后的文件名 被压缩的文件或者文件夹

例如::

    rar a -v1024m foo.rar foo

此命令即为对foo文件夹进行分卷压缩，每卷的大小为1024m，压缩后的文件名为foo.rar

2.解压

对任何一个分卷执行::

    rar e foo.part1.rar

使用tar

1.分卷压缩::

    tar cvzpf - foo | split -d -b 50m

上面的命令是将foo这个文件夹分卷压缩，每卷50m，注意foo前面有空格.压缩完之后，
会被命名为x00,x01,x02,...。

2.解压

首先需要合并， 然后解压::

    cat x*>foo.tar.gz
    tar xzvf foo.tar.gz


参考
====

* `Seven things about Linux you may not have known so far`_ （`中文翻译`_）

.. _Seven things about Linux you may not have known so far: https://opensourceforu.com/2017/09/top-7-things-linux-may-not-known-far/
.. _中文翻译: http://www.oschina.net/news/89404/top-7-things-linux-may-not-known-far
