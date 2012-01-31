#-*- coding:utf-8 -*-
from django.contrib import admin
from students.models import Student, Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('fio', 'number', 'student_group')
    ordering = ('fio',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','head_student')
    ordering = ('title',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)

