#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'scumer'
SITENAME = u"SCUMER"
SITEURL = 'http://localhost:8000'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh_CN'
DATE_FORMATS = {'en': '%b %d, %Y'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (('Email', 'mailto:scumer@126.com'),)

# Social widget
SOCIAL = (('Email', 'mailto:scumer@126.com'),
		  ('instagram', 'https://www.instagram.com/hi.scumer/'),
          )
		  
# Mailchimp
EMAIL_FIELD_PLACEHOLDER = u'scumer@126.com'	

# plugin
PLUGIN_PATHS = ['../pelican/pelican-plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'assets', 'series','neighbors', ]  
#'latex','liquid_tags.img',
#'share_post','related_posts',
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}				

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'
TYPOGRIFY = True


# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "../pelican/themes/pelican-elegant"
DUOSHUO_SITENAME = "scumer"

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

USE_SHORTCUT_ICONS = True