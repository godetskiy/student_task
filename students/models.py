#-*- coding:utf-8 -*-
from django.db import models

class Student(models.Model):
    fio = models.CharField(max_length=50)
    birth_date = models.DateField()
    number = models.CharField(max_length=50)
    student_group = models.ForeignKey('Group')

    def __unicode__(self):
        return self.fio

class Group(models.Model):
    title = models.CharField(u'Номер группы', max_length=10)
    head_student = models.ForeignKey(Student, blank=True, null=True)

    def __unicode__(self):
        return self.title
