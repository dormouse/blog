==================
Sphinx Note
==================

:date: 2013-09-10
:modified: 2021-03-31
:slug: sphinx-note
:tags: sphinx
:category: software
:author: Dormouse Young

reStructuredText 入门 
=======================
See http://www.sphinx-doc.org/en/stable/rest.html for more.

Here is a quick and dirty cheat sheet for some common stuff you want
to do in sphinx and ReST.

.. _formatting-text:

文本格式化
----------

=====  ====================     ============
名称   代码                     示例
=====  ====================     ============
斜体   ``*斜体*``               *斜体*
粗休   ``**粗体**``             **粗体**
原文   \`\`**原文**\`\`         ``**原文**``
=====  ====================     ============

源代码
------

末尾使用 ``::`` 符号，则下面的内容就显示为源代码,源代码需要缩进，例如::

    You can represent code blocks fairly easily::

       import numpy as np
       x = np.random.rand(12)

以上代码显示效果如下：

You can represent code blocks fairly easily::

   import numpy as np
   x = np.random.rand(12)

也可以直接从文件引入代码。例如从exts/chinese_search.py 引入代码可以使用如下命令::

    .. literalinclude:: exts/chinese_search.py

.. _making-a-list:

生成列表
--------

+------------------------+---------------------+
| 代码                   | 显示效果            |
+========================+=====================+
| ``* point A``          | * point A           |
|                        |                     |
| ``* point B``          | * point B           |
|                        |                     |
| ``* point C``          | * point C           |
|                        |                     |
+------------------------+---------------------+
| ``#. point A``         | #. point A          |
|                        |                     |
| ``#. point B``         | #. point B          |
|                        |                     |
| ``#. point C``         | #. point C          |
|                        |                     |
+------------------------+---------------------+

.. _making-a-table:

制作表格
--------

复杂表格写法如下::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

简单表格写法如下::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. _making-links:

制作链接
--------

```mysite <http://mysite.com>`_`` 显示为 `mysite <http://mysite.com>`_ 。

``http://www.mysite.com`` 直接显示为 http://www.mysite.com 。

``:ref:`making-a-table``` 用于引用文章内部章节。

``:mod:`matplotlib.backend_bases``` 用于引用模块。

``:class:`~matplotlib.backend_bases.LocationEvent``` 用于引用类。

``:meth:`~matplotlib.backend_bases.FigureCanvasBase.mpl_connect``` 用于引用方法。

划分章节
--------

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

全局替换
--------

reST支持“替换”，例如::

   .. |name| replace:: replacement *text*

或者::

   .. |caution| image:: warning.png
                :alt: Warning!

如果你想在所有文件使用中这些替换，一种方式是把它们写入 `rst_prolog` ；
另一种方式是把它们放到一个单独的文件中，然后在需要使用的文件中使用::

     :rst:dir:`include`

指令来导入这些替换。

Sphinx 内置的全局替换有 ``|today|`` 、 ``|release|`` 和 ``|version|`` 。

`today` 表示当前日期（时间），其显示格式可以通过 `conf.py` 文件中的 `today_fmt`
来设置。

图像
----

使用方法::

   .. image:: gnu.png
      (options)

When used within Sphinx, the file name given (here ``gnu.png``) must either be
relative to the source file, or absolute which means that they are relative to
the top source directory.  For example, the file ``sketch/spam.rst`` could refer
to the image ``images/spam.png`` as ``../images/spam.png`` or
``/images/spam.png``.

Sphinx will automatically copy image files over to a subdirectory of the output
directory on building (e.g. the ``_static`` directory for HTML output.)

Interpretation of image size options (``width`` and ``height``) is as follows:
if the size has no unit or the unit is pixels, the given size will only be
respected for output channels that support pixels (i.e. not in LaTeX output).
Other units (like ``pt`` for points) will be used for HTML and LaTeX output.

Sphinx extends the standard docutils behavior by allowing an asterisk for the
extension::

   .. image:: gnu.*

Sphinx then searches for all images matching the provided pattern and determines
their type.  Each builder then chooses the best image out of these candidates.
For instance, if the file name ``gnu.*`` was given and two files `gnu.pdf`
and `gnu.png` existed in the source tree, the LaTeX builder would choose
the former, while the HTML builder would prefer the latter.

脚注
^^^^

脚注用 ``[#name]_`` 来表示，在文档底部“ Footnotes ”标题后写具体内容::

   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

   .. rubric:: Footnotes

   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.

You can also explicitly number the footnotes (``[1]_``) or use auto-numbered
footnotes without names (``[#]_``).


Citations
^^^^^^^^^^

Standard reST citations  are supported, with the
additional feature that they are "global", i.e. all citations can be referenced
from all files.  Use them like so::

   Lorem ipsum [Ref]_ dolor sit amet.

   .. [Ref] Book or article reference, URL or whatever.

Citation usage is similar to footnote usage, but with a label that is not
numeric or begins with ``#``.


Comments
^^^^^^^^^

Every explicit markup block which isn't a valid markup construct (like the
footnotes above) is regarded as a comment .  For
example::

   .. This is a comment.

You can indent text after a comment start to form multiline comments::

   ..
      This whole indented block
      is a comment.

      Still in the comment.

Gotchas
^^^^^^^^

There are some problems one commonly runs into while authoring reST documents:

* **Separation of inline markup:** As said above, inline markup spans must be
  separated from the surrounding text by non-word characters, you have to use a
  backslash-escaped space to get around that.  See `the reference
  <http://docutils.sf.net/docs/ref/rst/restructuredtext.html#inline-markup>`_
  for the details.

* **No nested inline markup:** Something like ``*see :func:`foo`*`` is not
  possible.


Theme
=====

Install pydata theme
---------------------

The theme is available on PyPI and conda-forge, and can thus be installed with:

.. code:: console

    $ pip install pydata-sphinx-theme

.. code:: console

    $ conda install pydata-sphinx-theme --channel conda-forge

Then, in the ``conf.py`` of your sphinx docs, you update the ``html_theme``
configuration option:

.. code:: python

    html_theme = "pydata_sphinx_theme"


If you want to track the development version of the theme, you can
install it from the git repo:

.. code:: console

    $ pip install git+https://github.com/pydata/pydata-sphinx-theme.git@master

or in a conda environment yml file, you can add:

.. code:: none

    - pip:
      - git+https://github.com/pydata/pydata-sphinx-theme.git@master

More info : https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html


Install rtd theme
-----------------


The theme is available on PyPI and conda-forge, and can thus be installed with:

.. code:: console

    $ pip install sphinx_rtd_theme

Then, in the ``conf.py`` of your sphinx docs, you update the ``html_theme``
configuration option:

.. code:: python

    html_theme = "sphinx_rtd_theme"

More info : https://github.com/rtfd/sphinx_rtd_theme


使用 Sphinx 生成 PDF 文件
=========================

:date: 2013-01-27 21:42:37
:modified: 2021-03-15
:tags: sphinx, xetex, pdf, reStructuredText, markdown
:category: software
:slug: rst-pdf
:author: Dormouse Young
:summary: how to make pdf with Sphinx and reStructuredText(or markdown)


简介
----

本文主要说明如何使用 Sphinx 来生成 PDF 文件。

Sphinx 是一个可以把一系列 reStructuredText 格式文档转换为多种不同格式文档的工具。它具有
自动解决交叉引用和编制目录等功能。
Sphinx 支持 html 、 LaTeX 、 ePub 等多种输出格式。
现在 Sphinx 已支持 Markdown 格式的源文件。


安装编译环境
------------

本文的测试环境为 macOS Sierra 10.12.6, Python 3.6.1 。

#. 因为 Sphinx 需要 Python 2.7 或者 Python 3.4 以上版本的 Python ，所以首先
   要检查系统的 Python 是否安装， Python 的版本是否符合要求。如果想要使用
   Python3 ， macOS 下建议使用 brew 安装， Linux 下建议使用 Anaconda 。


#. 首先我们创建并激活一个 Python3 虚拟环境。打开终端，输入如下命令：

   ::

       $ python3 -m venv rst_pdf
       $ cd rst_pdf
       $ source bin/activate

   激活虚拟环境后提示符最前面会出现 ``(rst_pdf)`` 字样。


#. 安装 Sphinx-doc ：

   ::

      pip install -U Sphinx

#. 安装 LaTeX 支持。 macOS 下建议安装 MacTeX ，
   安装命令为 ``brew cask install mactex`` ，或者到
   https://www.tug.org/mactex/mactex-download.html 下载 MacTeX.pkg 后运行安装。
   注意这个安装包在大小约有 3.14 G 。
   Linux 下建议安装 `TeX Live <https://tug.org/texlive/>`_ 。


编写文档
--------

创建一个 Sphinx 项目，运行 ``sphinx-quickstart`` 命令::

    $ sphinx-quickstart

这个命令会提出一系列的问题来帮助我们进行项目的设置，
每个问题都有默认答案，如果想使用默认答案或者不知道如何回答，那么直接按回车键就可以了。
不用担心回答错误，以后可以通过修改配置文件来变更相关设置。
以下就是问题示例::

    Welcome to the Sphinx 1.6.4 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Enter the root path for documentation.
    > Root path for the documentation [.]:

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y
    说明：因为我们使用了 Python3 虚拟环境，所以这里我们选择把源文件单独存放在一个目录中。

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]:

    The project name will occur in several places in the built documentation.
    > Project name: rst_pdf
    > Author name(s): Dormouse Young

    Sphinx has the notion of a "version" and a "release" for the
    software. Each version can have multiple releases. For example, for
    Python the version is something like 2.5 or 3.0, while the release is
    something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
    just set both to the same value.
    > Project version []:
    > Project release []:

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    http://sphinx-doc.org/config.html#confval-language.
    > Project language [en]: zh_CN

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]:

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]:

    Sphinx can also add configuration for epub output:
    > Do you want to use the epub builder (y/n) [n]:

    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc: automatically insert docstrings from modules (y/n) [n]:
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]:
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
    > coverage: checks for documentation coverage (y/n) [n]:
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
    > viewcode: include links to the source code of documented Python objects (y/n) [n]:
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (y/n) [y]: y
    > Create Windows command file? (y/n) [y]: n

    Creating file ./source/conf.py.
    Creating file ./source/index.rst.
    Creating file ./Makefile.

    Finished: An initial directory structure has been created.

    You should now populate your master file ./source/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
       make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.



你会发现目录中生成了两个目录和一个文件。
``build`` 目录用于存放输出的内容，比如我们以后要生成的 PDF 文件。
``source`` 目录用于存放用户的源文件。
``Makefile`` 是项目工程文件，方便我们以后生成各种格式的文件。

``source`` 目录下有以下两个目录和两个文件。
``_static`` 目录用于存放用户自定义样式表或者其他静态文件。
``_templates`` 目录用于存放用户自定义的模版。
``conf.py`` 是项目配置文件，以后可以通过修改其中的内容来配置我们的项目。
``index.rst`` 是项目的索引文件，每个 sphinx-doc 项目都至少有一个索引文件。

为了能够正确的生成中文 PDF 文件，我们需要修改 ``conf.py`` 的
``Options for LaTeX output`` 一节中的 ``latex_elements`` 变量，修改为以下内容：
::

    latex_elements = {
        'papersize': 'a4paper',
        'preamble': '''
    \\usepackage{xeCJK}
    \\usepackage{indentfirst}
    \\setlength{\\parindent}{2em}
    \\setCJKmainfont{WenQuanYi Zen Hei Sharp}
    \\setCJKmonofont[Scale=0.9]{WenQuanYi Zen Hei Mono}
    \\setCJKfamilyfont{song}{WenQuanYi Zen Hei}
    \\setCJKfamilyfont{sf}{WenQuanYi Zen Hei}
    ''',
    }

现在可以在 ``source`` 目录下添加我们自己的 reStructuredText 文件。例如本文
的源文件就是 ``rst_pdf`` 文件。

写完后要修改 ``index.rst`` 文件，把新添加的 ``rst`` 文件加入目录树。例如本文的
``index.rst`` 内容为：
::

    Welcome to rst_pdf's documentation!
    ===================================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       rst_pdf

这里扩展名可以省略。

生成 PDF 文件
-------------

在项目根目录下使用 ``make latex`` 命令生成 tex 文件。修改文件中的字体，把
其中的 ``.otf`` 都改为 ``.ttf`` ::

    \setmainfont{FreeSerif}[
      Extension      = .ttf,
      UprightFont    = *,
      ItalicFont     = *Italic,
      BoldFont       = *Bold,
      BoldItalicFont = *BoldItalic
    ]
    \setsansfont{FreeSans}[
      Extension      = .ttf,
      UprightFont    = *,
      ItalicFont     = *Oblique,
      BoldFont       = *Bold,
      BoldItalicFont = *BoldOblique,
    ]
    \setmonofont{FreeMono}[
      Extension      = .ttf,
      UprightFont    = *,
      ItalicFont     = *Oblique,
      BoldFont       = *Bold,
      BoldItalicFont = *BoldOblique,
    ]

最后在 ``build/latex/`` 目录下运行 **两遍** ``xelatex rst_pdf.tex`` 命令即
可生成 PDF 文件。



让 Sphinx 支持 markdown
========================

`Markdown`__ is a lightweight markup language with a simplistic plain text
formatting syntax.  It exists in many syntactically different *flavors*.  To
support Markdown-based documentation, Sphinx can use `recommonmark`__.
recommonmark is a Docutils bridge to `CommonMark-py`__, a Python package for
parsing the `CommonMark`__ Markdown flavor.

__ https://daringfireball.net/projects/markdown/
__ https://recommonmark.readthedocs.io/en/latest/index.html
__ https://github.com/rtfd/CommonMark-py
__ https://commonmark.org/

Configuration
-------------

To configure your Sphinx project for Markdown support, proceed as follows:

#. Install the Markdown parser *recommonmark*::

      pip install --upgrade recommonmark

   .. note::

      The configuration as explained here requires recommonmark version
      0.5.0 or later.

#. Add *recommonmark* to the
   :confval:`list of configured extensions <extensions>`::

      extensions = ['recommonmark']

   .. versionchanged:: 1.8
      Version 1.8 deprecates and version 3.0 removes the ``source_parsers``
      configuration variable that was used by older *recommonmark* versions.

#. If you want to use Markdown files with extensions other than ``.md``, adjust
   the :confval:`source_suffix` variable.  The following example configures
   Sphinx to parse all files with the extensions ``.md`` and ``.txt`` as
   Markdown::

      source_suffix = {
          '.rst': 'restructuredtext',
          '.txt': 'markdown',
          '.md': 'markdown',
      }

#. You can further configure *recommonmark* to allow custom syntax that
   standard *CommonMark* doesn't support.  Read more in the `recommonmark
   documentation`__.

__ https://recommonmark.readthedocs.io/en/latest/auto_structify.html


一些 Tips
==============================================

Linux 下安装 TeX Live
------------------------------------------

方法一是使用 ``apt-get install texlive-full`` 命令安装。

方法二是
去 tex 的 `老家 <http://www.tug.org/texlive/acquire-netinstall.html>`_ 下载
`install-tl-unx.tar.gz <http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz>`_ 。

解压缩后，运行::

    sudo ./install-tl --gui=wizard

如果没有安装 wget ，则运行::

    sudo yum install wget

安装输出大致如下::

    输入 “In” 开始安装，一共有2599个项目......
    Actions:
    <I> start installation to hard disk
    <H> help
    <Q> quit

    Enter command: i
    Installing to: /usr/local/texlive/2012
    Installing [0001/2599, time/total: ??:??/??:??]: 12many [376k]
    Installing [0002/2599, time/total: 00:09/10:05:07]: 2up [66k]
    Installing [0003/2599, time/total: 00:10/09:32:46]: Asana-Math [458k]
    Installing [0004/2599, time/total: 00:12/05:36:55]: ESIEEcv [137k]
    Installing [0005/2599, time/total: 00:15/06:05:39]: FAQ-en [5765k]
    ......

    See /usr/local/texlive/2012/index.html
    for links to documentation.  The TeX Live web site
    contains updates and corrections: http://tug.org/texlive.

    TeX Live is a joint project of the TeX user groups around the world;
    please consider supporting it by joining the group best for you. The
    list of user groups is on the web at http://tug.org/usergroups.html.


    Add /usr/local/texlive/2012/texmf/doc/man to MANPATH, if not dynamically determined.
    Add /usr/local/texlive/2012/texmf/doc/info to INFOPATH.

    Most importantly, add /usr/local/texlive/2012/bin/x86_64-linux
    to your PATH for current and future sessions.

设置路径，把以下内容放在 .bash_profile 中，然后运行 . ~/.bash_profile(ubuntu
下是 ~/.bashrc)::

    PATH=$PATH:$HOME/.local/bin:$HOME/bin
    PATH=/usr/local/texlive/2012/bin/x86_64-linux:$PATH; export PATH
    MANPATH=/usr/local/texlive/2012/texmf/doc/man:$MANPATH; export MANPATH
    INFOPATH=/usr/local/texlive/2012/texmf/doc/info:$INFOPATH; export INFOPATH


如何查看系统中的字体
-----------------------------------------

在 macOS 中可以使用“字体册”应用来查看字体名称。
在 Linux 中可以用 ``fc-list`` 命令来获得字体名称。

