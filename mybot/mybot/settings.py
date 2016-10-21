# -*- coding: utf-8 -*-
BOT_NAME = 'mybot'

SPIDER_MODULES = ['mybot.spiders']
NEWSPIDER_MODULE = 'mybot.spiders'

ROBOTSTXT_OBEY = True

import sys
sys.path.insert(0, 'C:\Users\song\Desktop\django\myweb')    ####important####

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'

import django
django.setup()                      ###!!!!!###

ITEM_PIPELINES = {
    'mybot.pipelines.MybotPipeline': 1000,
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
FEED_URI = u'file:///C:/Users/song/Desktop/django/80s_allmovies.csv'
FEED_FORMAT = 'CSV'
