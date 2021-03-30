# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'Dormouse Blog'
copyright = '2011-2021, Dormouse Young'
author = 'Dormouse Young'

# The full version, including alpha/beta/rc tags
release = '1.1'
master_doc = 'index'
language = 'zh_CN'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['chinese_search', ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser', }
source_suffix = ['.rst', '.md']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DormouseBlogdoc'


# -- Options for LaTeX output ---------------------------------------------
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
    }
else:
    if sys.platform == 'linux':
        latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        #
            'papersize': 'a4paper',

        # The font size ('10pt', '11pt' or '12pt').
        #
        # 'pointsize': '10pt',

        # Additional stuff for the LaTeX preamble.
        #
            'preamble': '''
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont[BoldFont=WenQuanYi Micro Hei, ItalicFont=WenQuanYi Micro Hei]{WenQuanYi Micro Hei}
\setCJKsansfont[BoldFont=WenQuanYi Micro Hei Mono]{WenQuanYi Micro Hei Mono}
\setCJKmonofont{WenQuanYi Micro Hei Mono}
''',

        # Latex figure (float) alignment
        #
        # 'figure_align': 'htbp',

        # Additional stuff for the LaTeX preamble.

        }
    else:
        latex_elements = {
                'papersize': 'a4paper',
                'preamble': '''
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont[BoldFont=STFangsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
''',
        }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     'DormouseBlog.tex',
     'Dormouse Blog Documentation',
     'Dormouse Young',
     'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dormouseblog', 'Dormouse Blog Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DormouseBlog', 'Dormouse Blog Documentation',
     author, 'DormouseBlog', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ---------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



