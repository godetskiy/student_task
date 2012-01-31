from django.forms import ModelForm
from students.models import Student, Group

class StudentForm(ModelForm):
    class Meta:
        model = Student

class GroupForm(ModelForm):
    class Meta:
        model = Group