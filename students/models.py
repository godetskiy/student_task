#-*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Student(models.Model):
    fio = models.CharField(_(u'ФИО'),max_length=50)
    birth_date = models.DateField(_(u'Дата рождения'))
    number = models.CharField(_(u'Номер студенческого'),max_length=50)
    student_group = models.ForeignKey('Group', verbose_name=_(u'Группа'))

    class Meta:
        verbose_name = _(u'Студент')
        verbose_name_plural = _(u'Студенты')

    def __unicode__(self):
        return self.fio

class Group(models.Model):
    title = models.CharField(_(u'Номер группы'), max_length=10)
    head_student = models.OneToOneField(Student, blank=True, null=True, verbose_name=_(u'Староста'))

    class Meta:
        verbose_name = _(u'Группа')
        verbose_name_plural = _(u'Группы')

    def __unicode__(self):
        return self.title
