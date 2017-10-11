======================
安装 Linux Mint
======================

:date: 2012-04-25
:modified: 2014-10-16 20:31:00
:slug: install-linuxmint
:tags: linuxmint
:category: linux
:author: Dormouse Young

硬盘安装 Linux Mint 12
======================

Date: 2012-04-25

修改 Grub
------------

修改 /boot/grub/grub.cfg ，添加内容如下::

    ### 我把ISO放在C盘(第一硬盘第一分区)对应的是(hd0,1)

    menuentry "硬盘安装 Linux Mint 12″  –class linuxmint {
            insmod ntfs
            loopback loop (hd0,5)/linuxmint-12-gnome-dvd-32bit.iso
            linux (loop)/casper/vmlinuz boot=casper iso-scan/filename=/linuxmint-12-gnome-dvd-32bit.iso locale=zh_CN.UTF-8 noprompt noeject splash
            initrd (loop)/casper/initrd.lz
    }

添加 163 源
------------

在 /etc/apt/souce.list 文件中添加如下内容::

    deb http://mirrors.163.com/ubuntu/ oneiric main universe restricted multiverse
    deb-src http://mirrors.163.com/ubuntu/ oneiric main universe restricted multiverse
    deb http://mirrors.163.com/ubuntu/ oneiric-security universe main multiverse restricted
    deb-src http://mirrors.163.com/ubuntu/ oneiric-security universe main multiverse restricted
    deb http://mirrors.163.com/ubuntu/ oneiric-updates universe main multiverse restricted
    deb http://mirrors.163.com/ubuntu/ oneiric-proposed universe main multiverse restricted
    deb-src http://mirrors.163.com/ubuntu/ oneiric-proposed universe main multiverse restricted
    deb http://mirrors.163.com/ubuntu/ oneiric-backports universe main multiverse restricted
    deb-src http://mirrors.163.com/ubuntu/ oneiric-backports universe main multiverse restricted
    deb-src http://mirrors.163.com/ubuntu/ oneiric-updates universe main multiverse restricted

不用密码成为 Ubuntu 的 Root 用户
------------------------------------------------

编辑 vi /etc/pam.d/su ，将其中的::

    # auth sufficient pam_wheel.so trust

改为::

    auth sufficient pam_wheel.so trust group=admin

安装支持 PAE 的内核
-------------------------

Linux Mint 12 LXDE 只有32位的，且安装完后不支持 2G 以上内存。如果要支持 2G 以上
内存，那么要输入以下命令::

    sudo apt-get install linux-generic-pae linux-image-generic-pae linux-headers-generic-pae

安装常用软件
-----------------------

安装 python virtualenv ::

    apt-get install python-virtualenv

安装 virtualbox

下载 virtualbox 和 Extension
(https://www.virtualbox.org/wiki/Linux_Downloads) ,然后把用户添加到
vboxusers 组::

    usermod -a -G vboxusers dormouse

安装 vim ::

    apt-get install vim-gnome
    get vimim(http://vim.sourceforge.net/scripts/script.php?script_id=2506)
    get jidian wubi(http://code.google.com/p/vimim-data/downloads/detail?name=vimim.wubijd.txt.bz2&can=2&q=)
    cp vimim.vim ~/.vim/plugin/
    cp vimim.wubijd.txt ~/.vim/plugin/

vimim 使用方法：

    中文输入：gi

    英文输入：i

    输入方法切换：Ctrl+6


安装 XBMC

输入如下命令安装（ 适用于 Ubuntu 9.10 Karmic 或更高版本，详见：
http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Ubuntu/HOW-TO_1)::

    apt-get install python-software-properties pkg-config
    add-apt-repository ppa:team-xbmc
    apt-get update
    apt-get install xbmc xbmc-standalone
    apt-get update

安装完以后要设置字体：进入 XBMC，菜单 System -> Appearance -> Skin -> Fonts ->
选择 Arial based 。

安装其他软件 ::

    apt-get install build-essential python-wxtools wx2.8-doc wx2.8-examples
    apt-get install fcitx fcitx-table-wbpy stardict
    apt-get install keepassx amule gnucash geeqie
    apt-get install git-core git-gui git-doc

nevernote::

    sudo add-apt-repository ppa:vincent-c/nevernote
    sudo apt-get update
    sudo apt-get install nevernote


Linux Mint 17 安装笔记
======================

date: 2014-10-16 20:31:00

Install cloudstation
-------------------------------------------

* Download cloudstation
* Uncompress
* ./install

Select software source
-------------------------------------------

Select the fastest software source

Install some software
-------------------------------------------

* Install following software::

    sudo apt-get install build-essential python-dev
    sudo apt-get install fcitx fcitx-ui-classic fcitx-table-wbpy
    sudo apt-get install git vim-gnome ctags keepassx filezilla

* Software setup

    * Sync firefox

    * Setup git, see : `Github Setup <{filename}github-setup.rst>`_

Install virtualenv
-------------------------------------------

* Install pip and virtualenvwrapper::

    sudo apt-get install python-pip
    sudo pip install virtualenvwrapper

* Add flowing to ~/.bashrc::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/project
    source /usr/local/bin/virtualenvwrapper.sh
    reload .bashrc


Install XBMC
-------------------------------------------

输入如下命令安装（适用于 Ubuntu 9.10 Karmic 或更高版本，详见：
`Install_XBMC_on_Ubuntu/HOW-TO
<http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Ubuntu/HOW-TO_1>`_
）::

    sudo apt-get install python-software-properties pkg-config
    sudo add-apt-repository ppa:team-xbmc
    sudo apt-get update
    sudo apt-get install xbmc xbmc-standalone

安装完以后要设置字体：进入 XBMC，菜单 System -> Appearance -> Skin -> Fonts ->
选择 Arial based 。

