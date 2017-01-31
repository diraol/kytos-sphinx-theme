"""Kytos Sphinx Theme.

From https://github.com/kytos/kytos-sphinx-theme
"""
import os

__version__ = '0.1.0-alpha'
__version_full__ = __version__

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return [cur_dir]

# Conf.py import settings
html_theme = 'kytos_theme'
html_theme_path = get_html_theme_path()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'references'

# General information about the project.
version = __version__
release = __version__
show_version = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_static/css', '_static/images', '_static/js',
'_static/fonts']

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = None

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc_sidebar.html']}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'kytosdoc'

# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'kytos', u'Kytos Documentation',
        author, 'kytos', 'One line description of project.',
        'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
# Note: links to Python doc only work if you are online or have python.inv
#     file. To download it, run:
#     curl https://docs.python.org/3/objects.inv >python.inv
intersphinx_mapping = {
   'python': ('https://docs.python.org/3.5',
       (None, 'python.inv')),
   'kyco': ('http://docs.kytos.io/kyco',
       (None, 'kyco.inv')),
   'pyof': ('http://docs.kytos.io/python-openflow',
       (None, 'pyof.inv')),
   'kyco-core-napps': ('http://docs.kytos.io/kyco-core-napps',
       (None, 'kyco-core-napps.inv'))
}
# Napoleon settings from http://www.sphinx-doc.org/en/stable/ext/napoleon.html
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_special_with_doc = False  # Sphinx's default

# As pylint warns when the public __init__ is not documented (according to a
# PEP), we should document __init__ and the option below appends its docstring
# to the class'.
autoclass_content = 'both'

# Order methods before attributes/properties on a class
autodoc_member_order = 'groupwise'
todo_include_todos = True
