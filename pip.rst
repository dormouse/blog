============
Pip Note
============

使用国内镜像源来加速python pypi包的安装
=======================================

:create: 2015年 06月 08日 星期一 19:26:36 CST
       

pipy 国内镜像目前有：

* http://pypi.douban.com/  豆瓣

* http://pypi.hustunique.com/  华中理工大学

* http://pypi.sdutlinux.org/  山东理工大学

* http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学

可以在pip后面跟 -i 来指定源，比如用豆瓣的源来安装web.py框架：

pip install web.py -i http://pypi.douban.com/simple

注意后面要有 `/simple` 目录！！！

要配制成默认的话，需要创建或修改配置文件（ linux 的文件在 `~/.pip/pip.conf` ，
windows 在 `%HOMEPATH%\pip\pip.ini` ），修改内容为::

    index-url = http://pypi.douban.com/simple

更多配置参数见：http://www.pip-installer.org/en/latest/configuration.html

