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

project = 'Dormouse Documentation'
copyright = '2011-2021, Dormouse Young'
author = 'Dormouse Young'

# The full version, including alpha/beta/rc tags
version = '1.1'
release = '2021.07.01'
master_doc = 'index'
language = 'zh_CN'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'chinese_search',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser', }
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
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
# html_theme = 'furo'
html_theme = "pydata_sphinx_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DormouseBlogdoc'


# -- Options for LaTeX output ---------------------------------------------
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



