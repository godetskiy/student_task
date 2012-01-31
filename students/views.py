#-*- coding:utf-8 -*-
from django.shortcuts import Http404, HttpResponseRedirect, render_to_response
from students.models import Student, Group
from students.forms import StudentForm, GroupForm
from django.core.context_processors import csrf

def groups(request):
    groups = Group.objects.all()
    list = []
    for group in groups:
        list.append(
            {'id': group.id,
             'title': group.title,
             'count': Student.objects.filter(student_group=group.id).count(),
             'head_student': group.head_student}
        )
    return render_to_response('groups.html', {'groups': list})

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

def students(request, id):
    try:
        group_id = int(id)
    except ValueError:
        raise Http404()
    students = Student.objects.filter(student_group=group_id)
    group_title = Group.objects.get(id=id).title
    return render_to_response('students.html', locals())

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
        form = StudentForm()
    c['form'] = form
    return render_to_response('form.html', c)

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
