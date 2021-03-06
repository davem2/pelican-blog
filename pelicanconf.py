#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Maranhao'
SITENAME = 'davidmaranhao.com'
SITEURL = ''
#GITHUB_URL = 'https://github.com/davem2'
#GITHUB_POSITION = 'left'

STATIC_PATHS = ['images','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

#TYPOGRIFY = True

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

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
#SOCIAL = (('GitHub', GITHUB_URL),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 30


PLUGIN_PATHS = ['/home/david/projects/pelican-plugins/']
PLUGINS = ['representative_image']
#PLUGINS = ['photos', 'representative_image','better_figures_and_images']


#PHOTO_LIBRARY = '/home/david/projects/website/content/images/photos'
#PHOTO_GALLERY = (1024, 1024, 80)
#PHOTO_ARTICLE = (760, 760, 80)
#PHOTO_THUMB = (192, 192, 60)
#PHOTO_EXIF_KEEP = True
#PHOTO_EXIF_COPYRIGHT_AUTHOR = 'David Maranhao'
#PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'

RESPONSIVE_IMAGES = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#THEME = "/home/david/projects/pelican-themes/blueidea/"
THEME = "/home/david/projects/website/theme/blueidea/"
#THEME = "/home/david/projects/pelican-themes/relapse/"
#THEME = "/home/david/projects/pelican-themes/storm/"
