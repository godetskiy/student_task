#-*- coding:utf-8 -*-
from django.contrib import admin
from students.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('fio', 'number', 'student_group')
    ordering = ('fio',)

class StudentInline(admin.TabularInline):
    model = Student

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','head_student')
    ordering = ('title',)
    inlines = [
        StudentInline,
    ]

class LogAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'model_id', 'action', 'time')
    ordering = ('-time',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Log, LogAdmin)
