#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

THEME = 'theme'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATH = 'plugin'
PLUGINS = ['googleplus_comments']

AUTHOR = u'Luiz F. A. de Prá'
SITENAME = u'luizdepra'
SITEURL = 'http://blog.luizdepra.com.br'
#SITEURL = ''

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/luizdepra'),
          ('linkedin', 'http://www.linkedin.com/in/luizdepra'),
          ('github', 'http://github.com/RawArkanis'),)

DEFAULT_PAGINATION = 15

GITHUB_USER = 'RawArkanis'

DISPLAY_CATEGORIES_ON_MENU = False

ADDTHIS_PROFILE = 'ra-52c2cdf877ec8326'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
