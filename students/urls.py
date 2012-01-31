from django.conf.urls.defaults import patterns, include, url

from students.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student_task.views.home', name='home'),
    url(r'^$', groups),
    url(r'^add/$', group_add),
    url(r'^edit/(\d{1,5})', group_edit),
    url(r'^delete/(\d{1,5})$', group_delete),
    url(r'^(\d{1,5})/$', students),
    url(r'^(\d{1,5})/add/$', student_add),
    url(r'^(\d{1,5})/edit/(\d{1,5})', student_edit),
    url(r'^(\d{1,5})/delete/(\d{1,5})', student_delete),
)
