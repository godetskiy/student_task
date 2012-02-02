#-*- coding:utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver


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

class Log(models.Model):
    ACTION = (
        ('c', 'create'),
        ('e', 'edit'),
        ('d', 'delete'),
    )
    model_name = models.CharField(_(u'Имя модели'),max_length=10)
    model_id = models.PositiveIntegerField(_(u'id объекта'))
    action = models.CharField(_(u'Действие'),max_length=1, choices=ACTION)
    time = models.DateTimeField(_(u'Дата/Время'),)

    class Meta:
        verbose_name = _(u'Лог')
        verbose_name_plural = _(u'Логи')

    def __unicode__(self):
        return u'%s %s %s' %(model_name, model_id, action)


@receiver(post_save, sender=Student)
@receiver(post_save, sender=Group)
def create_edit_handler(instance, created, **kwargs):
    action = 'c' if created else 'e'
    ctype = ContentType.objects.get_for_model(instance)
    l = Log(model_name=ctype.model.title().encode(), model_id=ctype.id, action=action, time=datetime.now())
    l.save()

@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def delete_handler(instance, **kwargs):
    ctype = ContentType.objects.get_for_model(instance)
    l = Log(model_name=ctype.model.title().encode(), model_id=ctype.id, action='d', time=datetime.now())
    l.save()
