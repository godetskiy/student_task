from django.shortcuts import Http404, HttpResponseRedirect, render_to_response
from students.models import Student, Group

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

def students(request, id):
    try:
        group_id = int(id)
    except ValueError:
        raise Http404()
    students = Student.objects.filter(student_group=group_id)
    group_title = Group.objects.get(id=id).title
    return render_to_response('students.html', locals())