==================
Spyder in Winxp
==================

:date: 2013-11-21
:slug: spyder-on-winxp
:tags: pythonxy, pyzmq, spyder, windows
:category: software
:author: Dormouse Young
:summary: 在 Windows XP 下安装完 Python(x,y) 后无法运行 spyder 和 Ipython console 的解决方法

现象：在 Windows XP 下安装完 Python(x,y) 后无法运行 spyder 和 Ipython console 。

原因：新编译的 pyzmq 只支持 Windows Visa 以上版本，不支持 Windows XP。

解决：重新安装老版本的 `pyzmq
<https://pythonxy.googlecode.com/files/pyzmq-13.0.2-4_py27.exe>`_ 。

参考：https://code.google.com/p/pythonxy/issues/detail?id=670。

