#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rishi Sheth'
SITENAME = u'Rishi Sheth'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/rishiysheth'),
          ('github', 'https://github.com/physik932'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Chosen theme from pelican-themes
THEME = "/Users/rishi.sheth/p/pelican-themes/Flex"
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = "true"
THEME_COLOR_ENABLE_USER_OVERRIDE = "true"
PYGMENTS_STYLE = 'monokai'

SITESUBTITLE=""
SITELOGO="/images/me.jpg"

DISABLE_URL_HASH="true"
COPYRIGHT_YEAR = 2020