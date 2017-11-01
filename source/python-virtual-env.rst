*******************************
安装 Python 虚拟环境
*******************************

:date: 2012-04-25
:modified: 2017-09-25
:slug: python-virtual-env
:tags: python, virtual, venv, jupyter
:category: development
:author: Dormouse Young

Python3 Build-in
===================================

Python3 doc: https://docs.python.org/3/library/venv.html

Creation of virtual environments is done by executing the command venv::

    python3 -m venv /path/to/new/virtual/environment

Running this command will create ``bin/``, ``include/``, ``lib/`` and
``pyvenv.cfg`` in the path.

activate venv: ``$ source <venv>/bin/activate``

Anaconda
====================

Install
--------------------

官方网站：https://www.continuum.io/

conda 官方文档：https://docs.anaconda.com/

清华大学开源软件镜像站：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

安装清华大学仓库镜像，运行以下命令::

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes


常用命令
-------------------------

查看版本: ``conda -V`` 或者 ``conda --version``

查看信息: ``conda info``

查看当前环境的包列表: ``conda list``

搜索包: ``conda search beautifulsoup4``


虚拟环境
--------------------------

创建虚拟环境: ``conda create -n env_name package_name python=3*``

查看有哪些虚拟环境: ``conda env list``

查看当前所在的虚拟环境: ``conda info --e``

激活或切换虚拟环境： ``source activate env_name``

关闭虚拟环境： ``source deactivate``

移除虚拟环境： ``conda remove -n env_name --all``


如何在虚拟环境下使用 Jupyter book
-------------------------------------------------

This section is copy from https://stackoverflow.com/questions/38280739/how-to-make-conda-virtual-environments-persistent-and-available-for-tools-such-a

Register a (python) notebook kernel:

Let's suppose you have created a conda environment named jupyter-env35 with
conda create -n jupyter-env35 python=3.5 and now want to use it in jupyter.

Installing and registering a python kernel in the environment will make it
available over the graphical notebook interface.

To do so, first install the ipython kernel::

    conda install -n jupyter-env35 ipykernel

Then activate the environment and register the kernel::

    source activate jupyter-env35
    ipython kernel install --user --name jupyter-env35

When you now fire up juypter, it will show jupyter-env35 as a kernel in the
list of available kernels. If you select it, all packages installed into
juypter-env35 will be available.
Unregister a notebook kernel:

If you want delete the kernel from the notebook interface, ``jupyter --data-dir``, will print out jupyter's data directory.

Navigate to the printed folder, find the subfolder kernels and delete the folder with the name of your kernel (here jupyter-env35). After that the kernel will not show up in jupyter anymore.


使用 virtualenvwrapper
==================================

Install pip and virtualenvwrapper::

    sudo apt-get install python-pip
    sudo pip install virtualenvwrapper

Add flowing to ~/.bashrc::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/project
    source /usr/local/bin/virtualenvwrapper.sh

Reload it::

    reload .bashrc

Create virtualenv::

    cd project
    mkvirtualenv env_name

Create virtualenv with python3::

    mkvirtualenv -p python3 env_name

You should see something like::

    (env_name)dormouse@dormouse ~ $

Usage::

    mkvirtualenv [env] 创建新的虚拟环境
    workon [env]切换环境，如果不带环境名参数，则显示当前使用的环境
    deactivate 在某个环境中使用，切换到系统的python环境
    showvirtualenv [env] 显示指定环境的详情。
    lssitepackages 显示该环境中所安装的包
    rmvirtualenv [env] 移除指定的虚拟环境，移除的前提是当前没有在该环境中工作。
    cpvirtualenv [source] [dest] 复制一份虚拟环境。
    cdvirtualenv [subdir] 把当前工作目录设置为所在的环境目录。
    cdsitepackages [subdir] 把当前工作目录设置为所在环境的sitepackages路径。
    add2virtualenv [dir] [dir] 把指定的目录加入当前使用的环境的path中，这常使用于在多个project里面同时使用一个较大的库的情况。
    toggleglobalsitepackages -q 控制当前的环境是否使用全局的sitepackages目录。

Do some "pip install ..."

Freeze requirements::

    pip freeze > requirements.txt

Use pip to install later::

    pip install -r requirements.txt


使用 virtualenv
===============================

如果你使用 Mac OS X 或 Linux ，那么可以使用下面两条命令中任意一条::

    $ sudo easy_install virtualenv

或更高级的::

    $ sudo pip install virtualenv

上述命令中的任意一条就可以安装好 virtualenv 。也可以使用软件包管理器，在
Ubuntu 系统中可以试试::

    $ sudo apt-get install python-virtualenv

安装完 virtualenv ，打开一个 shell ，创建自己的环境。我通常创建一个包含 `env`
文件夹的项目文件夹::

    $ mkdir myproject
    $ cd myproject
    $ virtualenv env
    New python executable in env/bin/python
    Installing setuptools............done.

现在，每次需要使用项目时，必须先激活相应的环境。在 OS X 和 Linux 系统中运行::

    $ . env/bin/activate

（注意点和脚本名称之间有一个空格。点表示这个脚本必须运行在当前 shell 的背景中。
如果这个命令不能在你的 shell 中运行，请尝试把点替换为 ``source`` 。）

Windows 用户请运行下面的命令::

    $ env\scripts\activate

殊途同归，你现在进入你的 virtualenv （注意查看你的 shell 提示符已经改变了）。

