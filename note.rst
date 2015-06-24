======
随手记
======

pyqt4 示例所在目录::

    /usr/share/doc/python-qt4-doc/examples/sql

替换所有 python 文件内容示例::

    find . -name "*.py" | xargs sed -i "s/PySide/PyQt4/g"


同步资料
========

:date: 2015年 06月 02日 星期二 10:12:23 CST

同步一个目录到 U 盘示例::

    rsync -a --delete 编程资料2015 /media/dormouse/0078-63Aa/

参数说明

======== ==================================================================
参数     说明
======== ==================================================================
a        表示使用归档模式，相当于使用 -rlptgoD ，但不包括 -H 、 -A 、 -X
r        递归目录
l        复制符号链接
p        保留权限
t        保留修改时间
g        保留组
o        保留所有者
D        与 --devices --specials 相同
H        保留硬链接
A        保留权限（暗指 -p ）
X        保留扩展属性
delete   删除目的端多余的文件
devices  保留设备文件
specials 保留特定文件
======== ==================================================================

用 scp 同步远程文件::

    scp -r source_dir admin@11.22.33.44:/var/tmp/


ReText
======

:date: 2015年 03月 18日 星期三 10:02:54 CST

安装 ReText::

    sudo apt-get install retext
    sudo apt-get install python3-docutils python3-markdown python3-pygments python3-enchant

ReText 是一个使用python qt 写的 Markdown 编辑器。

ReText 依赖： python3-markups python3-pyqt4 python3-sip


Brickset 注册
=============

:date: 2014年 10月 23日 星期四 22:20:58 CST

Write to brickset.com ,and my project name is LM_LEGO.


手机联电脑
==========

:date: 2014年 10月 23日 星期四 21:13:09 CST

安装 adb 后，手机联上电脑后可以看见 SD 卡::

    sudo apt-get install android-tools-adb



