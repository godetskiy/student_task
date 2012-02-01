#-*- coding:utf-8 -*-
from django import settings

def AddDjangoSettings(request):
    return {
        'settings': settings,
    }