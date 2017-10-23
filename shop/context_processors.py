#!/usr/bin/env python
# encoding: utf-8


#from django.conf import settings
from django.conf import settings

def seo_processor(requests):
    return {
        'MEDIA_URL': '/media/',
        'SITE_URL': settings.SITE_URL,
        'CATEGORY_ID_TIANPIN': settings.CATEGORY_ID_TIANPIN,
        'CATEGORY_ID_JIANGUO': settings.CATEGORY_ID_JIANGUO,
    }
