*******************************
Conda & Anaconda
*******************************

:date: 2018-01-17
:modified: 2018-01-17
:slug: conda-anaconda
:tags: conda, anaconda
:category: software
:author: Dormouse Young


Conda是一个包管理器， Anaconda 是一个 python 发行版。

参考：

* 官方网站：https://www.continuum.io/
* conda 官方文档：https://docs.anaconda.com/
* `Conda: Myths and Misconceptions <https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>`_ (`中文翻译 <http://nooverfit.com/wp/%e5%85%b3%e4%ba%8econda%e5%92%8canaconda%e4%b8%8d%e5%8f%af%e4%b8%8d%e7%9f%a5%e7%9a%84%e4%ba%8b%e5%ae%9e%e5%92%8c%e8%af%af%e8%a7%a3-conda%e5%bf%85%e7%9f%a5%e5%bf%85%e4%bc%9a/>`_)


设置国内镜像源
=================================

清华大学开源软件镜像站：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

方法一：

安装清华大学仓库镜像，运行以下命令::

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes

方法二：

修改 ``~/.condarc`` 内容如下::

    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
      - defaults
    ssl_verify: true
    show_channel_urls: true


常用命令
=============================

查看版本: ``conda -V`` 或者 ``conda --version``

查看信息: ``conda info``

查看当前环境的包列表: ``conda list``

搜索包: ``conda search beautifulsoup4``

安装包: ``conda install beautifulsoup4``

更新包: ``conda update beautifulsoup4``

更新所有的包::

    conda update conda
    conda update anaconda
    conda updata --all


.. _venv-in-conda:

虚拟环境
================================

创建虚拟环境: ``conda create -n env_name package_name python=3*``

查看有哪些虚拟环境: ``conda env list``

查看当前所在的虚拟环境: ``conda info --e``

激活或切换虚拟环境： ``source activate env_name``

关闭虚拟环境： ``source deactivate``

移除虚拟环境： ``conda remove -n env_name --all``


如何在虚拟环境下使用 Jupyter book
==========================================================

This section is copy from
`stackoverflow questions 38280739 <https://stackoverflow.com/questions/38280739/how-to-make-conda-virtual-environments-persistent-and-available-for-tools-such-a>`_

Register a (python) notebook kernel
----------------------------------------------------------

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

Unregister a notebook kernel
----------------------------------------------------------

If you want delete the kernel from the notebook interface, ``jupyter
--data-dir``, will print out jupyter's data directory.

Navigate to the printed folder, find the subfolder kernels and delete the
folder with the name of your kernel (here jupyter-env35). After that the
kernel will not show up in jupyter anymore.
