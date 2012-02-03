#-*-coding: utf-8 -*-
from django.core.management.base import AppCommand

class Command(AppCommand):

    help = 'Print a list of groups and students in them'

    requires_model_validation = True

    def handle(self, *args, **options):
        from students.models import Student, Group
        groups = Group.objects.all()
        lines = []
        for group in groups:
            str = "%s: " % group.title
            for stud in group.student_set.all():
                str += "%s; " % stud.fio
            str += '\n'
            lines.append(str)
        return "".join(lines)