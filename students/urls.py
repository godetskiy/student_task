from django.conf.urls.defaults import patterns, include, url

from students.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student_task.views.home', name='home'),
    url(r'^$', groups),
)
