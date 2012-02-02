"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
#-*- coding:utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from students.models import Group
from datetime import date

class SimpleTest(TestCase):
    username = 'user'
    password = 'user'
    email = 'user@example.com'

    def setUp(self):
        User.objects.create_superuser(username=self.username, email=self.email, password=self.password)

    def test_basic_students(self):
        c = Client()

        actual = c.login(username=self.username, password=self.password)
        self.assertEqual(actual, True)

        test_title = 'Test group'
        actual = c.post('http://testserver/add/', {'title': test_title,}).status_code
        self.assertEqual(actual, 302)

        test_group = Group.objects.get(title=test_title).id

        link = 'http://testserver/' + str(test_group) + '/add/'
        actual = c.post(link, {'fio': 'Test student',
                               'birth_date': date.today(),
                               'number': '10005',
                               'student_group': test_group,})
        self.assertEqual(actual.status_code, 302)

