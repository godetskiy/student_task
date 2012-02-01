#-*- coding:utf-8 -*-
from django.shortcuts import Http404, HttpResponseRedirect, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.views.generic import list_detail
from django.contrib.auth.decorators import login_required

from students.models import Student, Group
from students.forms import StudentForm, GroupForm


def groups(request):
   return list_detail.object_list(request,
       queryset = Group.objects.all(),
       template_name = 'groups.html',
       template_object_name = 'groups',
   )

def students(request, id):
    group = get_object_or_404(Group, id=id)
    return list_detail.object_list(request,
        queryset = Student.objects.filter(student_group=id),
        template_name = 'students.html',
        template_object_name = 'students',
        extra_context= {'group_title': group.title}
    )

@login_required()
def group_add(request):
    c = {}
    c.update(csrf(request))
    c['title'] = u'Добавление новой группы'
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupForm()
    c['form'] = form
    return render_to_response('form.html', c)

@login_required()
def group_edit(request, group_id):
    c = {}
    c.update(csrf(request))
    c['title'] = u'Редактирование данных группы'
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupForm(instance=group)
    c['form'] = form
    return render_to_response('form.html', c)

@login_required()
def group_delete(request, group_id):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        group = Group.objects.get(id=group_id)
        group.delete()
        return HttpResponseRedirect('/')
    else:
        c['obj'] = u'группу'
        c['obj_title'] = Group.objects.get(id=group_id).title
    return render_to_response('delete.html', c)

@login_required()
def student_add(request, group_id):
    c = {}
    c.update(csrf(request))
    c['title'] = u'Добавление нового студента'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + group_id)
    else:
        form = StudentForm(initial={'student_group': group_id})
    c['form'] = form
    return render_to_response('form.html', c)

@login_required()
def student_edit(request, group_id, student_id):
    c = {}
    c.update(csrf(request))
    c['title'] = u'Редактирование данных студента'
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + group_id)
    else:
        form = StudentForm(instance=student)
    c['form'] = form
    return render_to_response('form.html', c)

@login_required()
def student_delete(request, group_id, student_id):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.delete()
        return HttpResponseRedirect('/' + group_id)
    else:
        c['obj'] = u'студента'
        c['obj_title'] = Student.objects.get(id=student_id).fio
    return render_to_response('delete.html', c)
