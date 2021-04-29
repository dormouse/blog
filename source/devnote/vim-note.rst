Vim Note
========

:date: 2017-02-10
:modified: 2021-03-31
:slug: vim-note
:tags: vim, note
:category: software
:author: Dormouse Young
:summary: Note for vim.

基本命令
--------

========== ============================================ ===========
命令       说明                                         分类
========== ============================================ ===========
0          行首                                         移动      
^          本行第一个非空字符                           移动      
$          行尾                                         移动      
`.         跳到最后修改的那一行                         移动      
'.         不仅跳到最后修改的那一行，还要定位到修改点   移动      
g;         循环跳转修改点(从最新的修改点开始)           移动      
g,         反向循环跳转修改点                           移动      
cw         删除一个单词并进入插入模式                   修改      
cc         删除一行并进入插入模式                       修改      
========== ============================================ ===========

命令行使用 MacVim
-----------------

Add following in ``./bash_profile``

    alias gvim='/Applications/MacVim.app/Contents/MacOS/Vim -g'

编辑多个文件
------------

打开文件
^^^^^^^^


在 vim 外部

- vim file1 file2 : open multiple files
- vim  -o file1 file2 : open multiple files with horizontal windows 
- vim  -O file1 file2 : open multiple files with vertical windows 

在 vim 内部

- :e file : open new file
- :sp file : open new file in hroizontal window
- :vs file : open new file in vertical window(same as :vsp, :vsplit)


关闭文件
^^^^^^^^

* ``:bd`` close current buffer
* ``:bd2`` close buffer No.2

切换文件
^^^^^^^^

* ``:ls`` show files list

在同一个窗口中切换缓冲区
^^^^^^^^^^^^^^^^^^^^^^^^

* ``Ctrl+6`` 两文件间的切换
* ``:bn`` 下一个文件
* ``:bp`` 上一个文件
* ``:ls`` 列出打开的文件，带编号
* ``:b1~n`` 切换至第n个文件

切换不同的窗口
^^^^^^^^^^^^^^^^

* ``Ctrl+w+方向键`` 切换到前／下／上／后一个窗格
* ``Ctrl+w+h/j/k/l`` 同上
* ``Ctrl+ww`` 依次向后切换到下一个窗格中

Shell
-----

- ``:shell`` open shell window. Use ``exit`` to quit shell window
- ``:!command`` run command in shell
- ``:r !command`` run command in shell, insert result to next line
  (ie: ``:r !date`` insert date to nex line)
- ``:3 !command`` 将文本中第三行的内容输入到命令command中进行处理，并将第三行的内容替换为命令的执行结果
- ``:1,3 !command`` 将文本中第一行到第三行的内容输入到命令command中进行处理，并将第一行到第三行的内容替换为命令的执行结果
- ``:3 w !command`` 将文本中第三行的内容输入到命令command中进行处理，不改变当前编辑文件的内容.
- ``1,3 w ``!command`` 将文本中第一行到第三行的内容输入到命令command中进行处理，不改变当前编辑文件的内容

什么是 ``<Leader>`` ？
---------------------------------

``<Leader>`` 默认为 ``\`` ，因此在按键映射中， ``<Leader>t`` 表示 ``\+t`` 。
可以通过 ``mapleader`` 变量来定义新的 ``<Leader>`` 。
如果 ``mapleader`` 未设置或者设置为空，那么就会使用默认的 ``\`` 。
在 VIM 中可以 ``:help leader`` 命令来获得相关帮助。

例如：

    :map <Leader>A  oanother line <Esc>

相当于：

    :map \A  oanother line <Esc>



但是当这样设置后：

    :let mapleader = ","

相当于：

    :map ,A  oanother line <Esc>

注意：
改变 ``mapleader`` 会导致以前的定义失效。

正则表达式
-----------

元字符
^^^^^^^^

元字符是具有特殊意义的字符。使用元字符可以表达 **任意字符** 、 **行首** 、
**行 尾** 、 **某几个字符** 等意义。

一些常用的元字符

============= ====================================================================
元字符        说明                                                         
============= ====================================================================
``.``         匹配任意一个字符,如 ``p*p`` 可以匹配字符串 ``pep``, ``pip``
``[abc]``     匹配方括号中的任意一个字符。可以使用-表示字符范围            
``[a-z0-9]``  匹配小写字母和阿拉伯数字                                     
``[^abc]``    在方括号内开头使用 ``^`` 符号，表示匹配除方括号中字符之外的任意字符 
``\d``        匹配阿拉伯数字，等同于 ``[0-9]``                                
``\D``        匹配阿拉伯数字之外的任意字符，等同于 ``[^0-9]``                 
``\x``        匹配十六进制数字，等同于 ``[0-9A-Fa-f]``                        
``\w``        匹配单词字母，等同于 ``[0-9A-Za-z_]``                           
``\W``        匹配单词字母之外的任意字符，等同于 ``[^0-9A-Za-z_]``            
``\t``        匹配 ``<TAB>`` 字符                                                
``\s``        匹配空白字符，等同于 ``[ \t]``                                  
``\S``        匹配非空白字符，等同于 ``[^ \t]``                               
``\a``        所有的字母字符. 等同于 ``[a-zA-Z]``                             
``\l``        小写字母 ``[a-z]``                                              
``\L``        非小写字母 ``[^a-z]``                                           
``\u``        大写字母 ``[A-Z]``                                             
``\U``        非大写字母 ``[^A-Z]``                                           
============= ====================================================================

另外，如果要查找字符 ``*`` 、 ``.`` 和 ``/`` 等，则需要在前面用 ``\`` 符号，
表示这不是元字符，而只是普通字符而已。

====== ===================
元字符 说明         
====== ===================
``\*`` 匹配 * 字符。
``\.`` 匹配 . 字符。
``\/`` 匹配 / 字符。
``\\`` 匹配 \ 字符。
``\[`` 匹配 [ 字符。
====== ===================

表示数量的元字符

========== ===============
元字符     说明        
========== ===============
``*``      匹配0-任意个
``\+``     匹配1-任意个
``\?``     匹配0-1个   
``\{n,m}`` 匹配n-m个   
``\{n}``   匹配n个     
``\{n,}``  匹配n-任意个
``\{,m}``  匹配0-m个   
========== ===============

表示位置的符号

============== ===========================================================
位置元字符     含义                                                        
============== ===========================================================
``$``          匹配行尾,如 ``here:$`` 只会匹配出位于一行结尾的 ``here:`` .         
``^``          匹配行首,如 ``^Part`` 只会匹配出位于一行开头的 ``Part`` .           
``\<`` ``\>``  会匹配出以某些字符开头的( ``\<`` )或结尾( ``\>`` )的单词。
============== ===========================================================

替换变量
^^^^^^^^

在正规表达式中使用 ``\(`` 和 ``\)`` 符号括起正规表达式，即可在后面使用
``\1`` 、 ``\2`` 等变量来访问 ``\(`` 和 ``\)`` 中的内容。

使用例

* ``/\(a\+\)[^a]\+\1`` 查找开头和结尾处a的个数相同的字符串，如 aabbbaa，aaacccaaa，但是不匹配 abbbaa
* ``:s/\(http:\/\/[-a-z\._~\+%\/]\+\)/<a href="\1">\1<\/a>/`` 将URL替换为<a href="http://url">http://url</a>的格式
* ``:s/\(\w\+\)\s\+\(\w\+\)/\2\t\1`` 将 data1 data2 修改为 data2 data1

贪婪模式和非贪婪模式
^^^^^^^^^^^^^^^^^^^^

在 Vim 里，默认是贪婪模式，即 ``a.*b`` 会尽可能多滴匹配字符，在
``ahdbjkbkls`` 中匹配 ``ahdbjkb`` 而不是 ``ahdb`` 。如果是非贪婪的，可以使用
``\{-}`` 代替 ``*``，即 ``a.\{-}b`` 匹配 ``ahdb`` 而不是 ``ahdbjkb`` 。

注释多行 python 代码
--------------------

将需要注释的代码以文档字符串的形式呈现
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

将需要注释的代码以函数的形式呈现
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用vim自身快捷键
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

增加多行注释

1. 首先按 ``ESC`` 进入命令行模式下，按下 ``CTRL + V`` ，进入列（也叫区块）模式。
2. 在行首使用上下键选择需要注释的多行。
3. 按下大写 ``I`` 键，进入插入模式。
4. 然后输入注释符（ ``//`` 、 ``#`` 等）。
5. 最后按下 ``Esc`` 键，稍等一会儿。

删除多行注释

1. 首先按 ``ESC`` 进入命令行模式下，按下 ``CTRL + V`` ，进入列模式。
2. 上下左右选定要取消注释的多行。
3. 按下 ``x`` 或者 ``d`` 。


Install Vundle
---------------

:date: 2017-02-08 18:57:00
:modified: 2017-02-08 18:57:00

Vundle is short for Vim bundle and is a Vim plugin manager.

Official site: https://github.com/VundleVim/Vundle.vim

Use following command to install Vundle::

    $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Put following lines at the top of your .vimrc to use Vundle. Remove plugins you
don't need, they are for illustration purposes::

    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'

    " The following are examples of different formats supported.
    " Keep Plugin commands between vundle#begin/end.
    " plugin on GitHub repo
    Plugin 'tpope/vim-fugitive'
    " plugin from http://vim-scripts.org/vim/scripts.html
    Plugin 'L9'
    " Git plugin not hosted on GitHub
    Plugin 'git://git.wincent.com/command-t.git'
    " git repos on your local machine (i.e. when working on your own plugin)
    Plugin 'file:///home/gmarik/path/to/plugin'
    " The sparkup vim script is in a subdirectory of this repo called vim.
    " Pass the path to set the runtimepath properly.
    Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
    " Install L9 and avoid a Naming conflict if you've already installed a
    " different version somewhere else.
    Plugin 'ascenator/L9', {'name': 'newL9'}

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    "filetype plugin on
    "
    " Brief help
    " :PluginList       - lists configured plugins
    " :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line


Two ways to Install Plugins
---------------------------

- Launch ``vim`` and run ``:PluginInstall``

- To install from command line: ``vim +PluginInstall +qall``


My .vimrc
---------

2017年 10月 12日 星期四 08:49:53 CST

There is my .vimrc::

    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'

    " The following are examples of different formats supported.
    " Keep Plugin commands between vundle#begin/end.


    " plugin on GitHub repo
    " for chinese input 
    Plugin 'vim-scripts/VimIM'
    " for file tree list
    Plugin 'scrooloose/nerdtree'
    " for comment quickly
    Plugin 'scrooloose/nerdcommenter'

    " plugin from http://vim-scripts.org/vim/scripts.html
    " taglist
    Plugin 'taglist.vim'

    " Git plugin not hosted on GitHub
    " Plugin 'git://git.wincent.com/command-t.git'
    " git repos on your local machine (i.e. when working on your own plugin)
    " Plugin 'file:///home/gmarik/path/to/plugin'
    " The sparkup vim script is in a subdirectory of this repo called vim.
    " Pass the path to set the runtimepath properly.
    " Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
    " Install L9 and avoid a Naming conflict if you've already installed a
    " different version somewhere else.
    " Plugin 'ascenator/L9', {'name': 'newL9'}

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    " filetype plugin on
    "
    " Brief help
    " :PluginList       - lists configured plugins
    " :PluginInstall    - installs plugins;
    "                     append `!` to update or just :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean      - confirms removal of unused plugins;
    "                     append `!` to auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line


    """""""""""""""
    " Key mapping "
    """""""""""""""
    map <F5> :!python %<CR>
    map <F8> :w<CR>:!python3 %<CR>
    map <C-n> :NERDTreeToggle<CR>
    map <C-t> :TlistToggle<CR>


    """"""""""""""""""
    " Plugin setting "
    """"""""""""""""""
    " NerdCommenter
    let g:NERDSpaceDelims = 1

    " Taglist
    let Tlist_Show_One_File = 1 " Only current file's tlist
    let Tlist_Exit_OnlyWindow = 1 " If only tlist left, then quit vim
    let Tlist_Auto_Open=1
    let Tlist_Use_Right_Window = 1 " Show in right window


    """""""""""""""""
    " Other setting "
    """""""""""""""""
    set autoindent
    " set columns=85
    set colorcolumn=80
    set expandtab 
    set foldmethod=syntax
    set foldmethod=indent
    set ignorecase
    set shiftwidth=4
    set tabstop=4 
    set lines=40
    set number
    set nobackup

    colorscheme slate

    "解决中文字符显示半个的问题
    set ambiwidth=double

    """""""""""""""""""""""""""""
    "解决windows下的中文乱码问题
    """""""""""""""""""""""""""""
    set encoding=utf-8
    "set termencoding=utf-8
    set fileencodings=ucs-bom,utf-8,chinese,latin-1
    if has("win32")
        set fileencoding=chinese
        "解决中文菜单乱码
        set langmenu=zh_CN.utf-8
        source $VIMRUNTIME/delmenu.vim
        source $VIMRUNTIME/menu.vim
        "解决console输出乱码
        language messages zh_cn.utf-8
        "设置字体
        "取得当前使用的字体：set guifont?
        "如果字体名称中含有空格，需要在空格前面加上一个反斜杠(\)：
        "set guifont=Terminal:h18:b:cANSI
        set guifont=Fixedsys
    else
        set fileencoding=utf-8
        set guifont=文泉驿等宽微米黑\ 12
    endif

    """""""""""""""""""""""
    " 设定 vimdiff 的颜色 "
    """""""""""""""""""""""
    if &diff
        set tw=80 columns=180
        " 设定超过的部份会自动换行，适合搭配显示行号使用
        " Add 代表新增的一行， Delete 代表删除的一行，
        " Change 代表有差异的一行，Text 代表有差异的这一行中，具有差异的部份
        hi DiffAdd ctermfg=Grey ctermbg=Blue guifg=Black guibg=LightBlue
        hi DiffDelete ctermfg=Grey ctermbg=Grey guifg=Grey
        hi DiffChange ctermfg=Black ctermbg=DarkGreen guifg=Black guibg=LightGray
        hi DiffText ctermfg=Black ctermbg=Grey guifg=Black guibg=Gray
    endif

参考
----

- Vim Doc: http://www.vim.org/docs.php
- Vim Cheat Sheet: https://vim.rtorr.com/
