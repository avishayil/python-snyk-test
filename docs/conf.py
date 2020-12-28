# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import traceback

import sphinx_py3doc_enhanced_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'Snyk Test'
year = '2020'
author = 'Avishay Bar'
copyright = '{0}, {1}'.format(year, author)
try:
    from pkg_resources import get_distribution
    version = release = get_distribution('snyk_test').version
except Exception:
    traceback.print_exc()
    version = release = '0.0.2'

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/avishayil/python-snyk-test/issues/%s', '#'),
    'pr': ('https://github.com/avishayil/python-snyk-test/pull/%s', 'PR #'),
}
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/avishayil/python-snyk-test/'
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
