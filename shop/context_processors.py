#!/usr/bin/env python
# encoding: utf-8


#from django.conf import settings
from ecshop import settings

def seo_processor(requests):
    return {
        'MEDIA_URL': '/media/',
    }
