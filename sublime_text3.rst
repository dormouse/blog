.. title: Use Sublime Text3
.. slug: use-sublime-text3
.. date: 2016-05-28 16:49:21 UTC+08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


==================
使用 sublime text3
==================

安装 Package Control
====================

https://packagecontrol.io/installation

在 sublime text3 的终端中运行如下代码安装 Package Control ，终端打开方法为
使用 ``ctrl+\``` 快捷键或者选择菜单 ``View > Show Console`` ::

    import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

通过 ``ctrl+shift+p`` 进入 ``Command Palette`` ，输入
``Package Contorl: Install Package`` (简写为 ``ip`` )，回车执行，
进入插件的搜索窗口，查找选择到需要的插件后，回车即可进行安装，
安装状态在最下面的状态栏内会有文字提示。
    
安装 Anaconda
=============

我的配置
========

配置如下::

    {
        "auto_complete": false,
        "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
        "ensure_newline_at_eof_on_save": true,
        "file_exclude_patterns":
        [
            ".DS_Store",
            "*.pid",
            "*.pyc"
        ],
        "find_selected_text": true,
        "fold_buttons": false,
        "folder_exclude_patterns":
        [
            ".git",
            "__pycache__"
        ],
        "font_face": "文泉驿等宽微米黑",
        "font_size": 12.0,
        "font_options":
        [
            "subpixel_antialias",
            "no_bold"
        ],
        "highlight_line": true,
        "ignored_packages":
        [
        ],
        "line_padding_bottom": 1,
        "line_padding_top": 1,
        "scroll_past_end": false,
        "show_full_path": true,
        "show_minimap": false,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true
    }
