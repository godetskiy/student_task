#-*- coding:utf-8 -*-
from django.conf import settings

def AddDjangoSettings(request):
    return {
        'settings': settings,
    }