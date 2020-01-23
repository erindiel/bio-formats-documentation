# -*- coding: utf-8 -*-
#
# Bio-Formats documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 29 15:42:49 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# Substitutions from external build system.
srcdir = '@sphinx_srcdir@'
builddir = '@sphinx_builddir@'
bioformats_source_branch = '@bioformats_source_branch@'
openmicroscopy_source_user = '@openmicroscopy_source_user@'
ome_source_user = '@ome_source_user@'
ome_common_version = '@ome_common_version@'
ome_model_version = '@ome_model_version@'
ome_model_uri = '@ome_model_uri@'
bf_version = '@bioformats.version@'

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(srcdir, '_ext')))
import re
import subprocess
from datetime import datetime


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.)
extensions = ['sphinx.ext.extlinks', 'edit_on_github']

## Configuration for the edit_on_github extension
edit_on_github_project = 'ome/bio-formats-documentation'
edit_on_github_branch = 'master'
edit_on_github_prefix = 'sphinx'

# Add any paths that contain templates here, relative to this directory.
templates_path = [os.path.join(srcdir, '_templates')]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bio-Formats'
title = u'%s Documentation' % project
author = u'The Open Microscopy Environment'
now = datetime.now()
copyright = u'2000-%d, %s ' % (now.year, author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.  Set on command-line or via ant build to real version.
#
version = 'UNKNOWN'
release = '@version@'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'CMakeLists.txt']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

github_root = 'https://github.com/'
bf_github_root = github_root + openmicroscopy_source_user + '/bioformats/'
bf_github_tree = bf_github_root + 'tree/' + bioformats_source_branch + '/'
bf_github_blob = bf_github_root + 'blob/' + bioformats_source_branch + '/'
gpl_formats = bf_github_blob + 'components/formats-gpl/src/loci/formats/'
bsd_formats = bf_github_blob + 'components/formats-bsd/src/loci/formats/'
bf_cpp = bf_github_blob + 'cpp/'

# Variables used to define other extlinks
cvs_root = 'http://cvs.openmicroscopy.org.uk'
trac_root = 'https://trac.openmicroscopy.org/ome'
oo_root = 'https://www.openmicroscopy.org'
lists_root = 'http://lists.openmicroscopy.org.uk'
downloads_root = 'https://downloads.openmicroscopy.org'
docs_root = 'https://docs.openmicroscopy.org'
imagesc_root = 'https://forum.image.sc'

extlinks = {
    # image.sc
    'imagesc' : (imagesc_root + '/%s', '#'),
    # Trac links
    'ticket' : (trac_root + '/ticket/%s', '#'),
    'milestone' : (trac_root + '/milestone/%s', ''),
    'report' : (trac_root + '/report/%s', ''),
    # Github links
    'source' : (bf_github_blob + '%s', ''),
    'sourcedir' : (bf_github_tree + '%s', ''),
    'bfreader' : (gpl_formats + 'in/%s', ''),
    'bsd-reader' : (bsd_formats + 'in/%s', ''),
    'bfwriter' : (gpl_formats + 'out/' + '%s', ''),
    'bsd-writer' : (bsd_formats + 'out/' + '%s', ''),
    'bf-cpp-lib': (bf_cpp + 'lib/' + '%s', ''),
    'doc_source' : ('https://github.com/ome/bio-formats-documentation/blob/master' + '/%s', ''),
    # Mailing list/forum links
    'mailinglist' : (lists_root + '/mailman/listinfo/%s', ''),
    'forum' : (oo_root + '/community/%s', ''),
    # Website links. Separating them out so that we can add prefixes and
    # suffixes during testing.
    'oo_root' : (oo_root + '/%s', ''),
    'community' : (oo_root + '/support/%s', ''),
    'omero' : (oo_root + '/omero/%s', ''),
    # Documentation
    'model_doc' : (docs_root + '/ome-model/' + ome_model_version + '/' + '%s', ''),
    'devs_doc' : (docs_root + '/contributing/%s', ''),


    # Miscellaneous links
    'doi' : ('http://dx.doi.org/%s', ''),
    'schema' : (oo_root + '/Schemas/Documentation/Generated/%s', ''),
    'examples' : (github_root + 'ome/bio-formats-examples/blob/master/%s', ''),
    'java_examples' : (github_root + 'ome/bio-formats-examples/blob/master/src/main/java/%s', ''),
    }

# Javadoc extlinks hosted on https://javadoc.io
OME_COMMON_JAVADOC = 'https://javadoc.io/page/org.openmicroscopy/ome-common/'
if ome_common_version.endswith('SNAPSHOT'):
    extlinks['common_javadoc'] = (OME_COMMON_JAVADOC + 'latest/%s', '')
else:
    extlinks['common_javadoc'] = (
        OME_COMMON_JAVADOC +  ome_common_version + '/%s', '')

OME_XML_JAVADOC = 'https://javadoc.io/page/org.openmicroscopy/ome-xml/'
if ome_model_version.endswith('SNAPSHOT'):
    extlinks['xml_javadoc'] = (OME_XML_JAVADOC + 'latest/%s', '')
else:
    extlinks['xml_javadoc'] = (
        OME_XML_JAVADOC +  ome_model_version + '/%s', '')

# Bio-Formats downloads
if bf_version.endswith('SNAPSHOT'):
    v = bf_version.split(".")
    if v[2] == "0-SNAPSHOT":
        if v[1] == "0":
            # x.0.0-SNAPHOT should point at /latest/bio-formats/
            suffix = ""
        else:
            # x.y.0-SNAPHOT should point at /latest/bio-formatsx/
            suffix = v[0]
    else:
        # x.y.z-SNAPHOT should point at /latest/bio-formatsx.y/
        suffix = ".".join(v[:2])
    bf_downloads_root = downloads_root + '/latest/bio-formats%s/' % suffix
else:
    bf_downloads_root = downloads_root + '/bio-formats/%s/' % bf_version

extlinks.update({
    'downloads' : (bf_downloads_root + '%s', ''),
    'javadoc' : (bf_downloads_root + 'api/%s', '')})

if ome_model_uri != "":
    extlinks['model_doc'] = (ome_model_uri + '/' + '%s', '')

rst_epilog = """
.. _Hibernate: http://www.hibernate.org
.. _ZeroC: http://www.zeroc.com
.. _Ice: http://www.zeroc.com
.. |JVM| replace:: :abbr:`JVM (Java Virtual Machine)`

.. |Poor| image:: /images/crystal-1.png
           :alt: 1 - Poor
.. |Fair| image:: /images/crystal-2.png
           :alt: 2 - Fair
.. |Good| image:: /images/crystal-3.png
           :alt: 3 - Good
.. |Very Good| image:: /images/crystal-4.png
                :alt: 4 - Very Good
.. |Outstanding| image:: /images/crystal-5.png
                  :alt: 5 - Outstanding
.. |no| image:: /images/crystal-no.png
         :alt: No
.. |yes| image:: /images/crystal-yes.png
          :alt: Yes

"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'
html_theme_options = {
    'rightsidebar': 'false',
    'stickysidebar': 'false',
    'footerbgcolor': '#cfd8dc',
    'footertextcolor': '#455a64',
    'sidebarbgcolor': '#cfd8dc',
    'sidebartextcolor': '#263238',
    'sidebarlinkcolor': '#455a64',
    'relbarbgcolor': '#263238',
    'relbartextcolor': '#ffffff',
    'relbarlinkcolor': '#ffffff',
    'bgcolor': '#ffffff',
    'textcolor': '#37474f',
    'linkcolor': '#1d8dcd',
    'visitedlinkcolor': '#1d8dcd',
    'headbgcolor': '#eceff1',
    'headtextcolor': '#263238',
    'headlinkcolor': '#009688',
    'codebgcolor': '#eceff1',
    'codetextcolor': '#455a64',
    'bodyfont': 'Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif',
    'headfont': 'Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.abspath(os.path.join(srcdir, 'images/ome.svg'))

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = { '**' : ['globalbftoc.html', 'pagetoc.html',
'relations.html', 'searchbox.html', 'sourcelink.html'] }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright …" is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bio-Formatsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'classoptions': ',oneside',
    'pointsize': '10pt',
    'inputenc': '%% Unused',
    'utf8extra': '%% Unused',
    'fontenc' : '%% Unused',
    'fontpkg': '%% Unused',
    'babel': '',
    'printindex': '''\\phantomsection
\\addcontentsline{toc}{part}{\indexname}
\\printindex''',
    'preamble': '''
\input{preamble.tex}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
target = project + '.tex'
latex_documents = [
  (master_doc, target, title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = os.path.join(srcdir, 'images/bio-formats-logo.pdf')

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
#man_pages = []

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, project, title, author, 'omedocs', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- Options for the linkcheck builder ----------------------------------------

# Timeout value, in seconds, for the linkcheck builder
linkcheck_timeout = int(os.environ.get("SPHINX_LINKCHECK_TIMEOUT", 30))
linkcheck_workers = int(os.environ.get("SPHINX_LINKCHECK_WORKERS", 5))
linkcheck_retries = int(os.environ.get("SPHINX_LINKCHECK_RETRIES", 5))

# Timeout value, in seconds, for the linkcheck builder
linkcheck_timeout = int(os.environ.get("SPHINX_LINKCHECK_TIMEOUT", 30))
linkcheck_workers = int(os.environ.get("SPHINX_LINKCHECK_WORKERS", 5))
linkcheck_retries = int(os.environ.get("SPHINX_LINKCHECK_RETRIES", 5))

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore = ['https://imspector.mpibpc.mpg.de',
    'https://www.olympus-global.com',
    'http://www.lavisionbiotec.com/',
    r'.*[.]sourceforge.net',
    r'http://www.libpng.org/.*',
    'https://nifti.nimh.nih.gov/nifti-1/',
    r'https://cbia.fi.muni.cz.*',
    r'https://www.fei.com/.*',
    r'https?://www.ionpath.com/.*',
    r'http://www.scanco.ch/',
    r'https://www.slf4j.org/',
    'http://cellularimaging.perkinelmer.com/downloads/',
    'https://animatedpngs.com/', # SSL certificate error
    'https://www.merckmillipore.com', # Read timeout
    r'https://www.nis-elements.com/.*', # Invalid SSL certificate
    r'https://www.nikoninstruments.com/.*', # Invalid SSL certificate
    r'http://farsight-toolkit.ee.uh.edu/.*',
    r'https://testng.org/*', # Invalid SSL certificate
    r'http://www.bio-rad.com/*', # 503 Server Error with Sphinx v1.8.5  
    r'https://www.mayo.edu/.*',
    r'https://libjpeg-turbo.org'
]
