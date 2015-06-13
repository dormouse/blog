Linux 软件安装
**************


=========================================
使用国内镜像源来加速 python pypi 包的安装  
=========================================

:date: 2015年 06月 13日 星期六 10:58:22 CST

pipy国内镜像目前有：

* http://pypi.douban.com/  豆瓣
* http://pypi.hustunique.com/  华中理工大学
* http://pypi.sdutlinux.org/  山东理工大学
* http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学

可以使用 -i 参数来指定源，比如用豆瓣的源来安装 web.py:: 

    pip install web.py -i http://pypi.douban.com/simple

.. attention::
    注意后面要有/simple目录。

要配制成默认的话，需要创建或修改配置文件（ linux 的文件在
~/.pip/pip.conf ， windows 在 %HOMEPATH%\pip\pip.ini ），修改内容为::

    [global]

    index-url = http://pypi.douban.com/simple

这样在使用pip来安装时，会默认调用该镜像。

更多配置参数见：http://www.pip-installer.org/en/latest/configuration.html


==================
Apt cheat sheet
==================


搜索 Apt 已安装的软件
=====================
ubuntu 下 apt-get install 完一个软件，想知道它装到哪里了用这个命令::

    dpkg -L python-qt4

