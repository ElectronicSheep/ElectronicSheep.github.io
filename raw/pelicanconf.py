#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Electronic Sheep'
SITENAME = u'Electronic Sheep'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './frankv-twenty-pelican-html5up'

def collectstatic():
  if os.path.isdir(DEPLOY_PATH):
    local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/'.format(**env))
    local('cp -rf {theme_path}/frankv-twenty-pelican-html5up/static/css/* {deploy_path}/css/'.format(**env))
    local('cp -rf {theme_path}/frankv-twenty-pelican-html5up/static/js/* {deploy_path}/js/'.format(**env))
    local('cp -rf {theme_path}/frankv-twenty-pelican-html5up/static/fonts/* {deploy_path}/fonts/'.format(**env))
    local('cp -rf {theme_path}/frankv-twenty-pelican-html5up/static/images/* {deploy_path}/images/'.format(**env))

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}
