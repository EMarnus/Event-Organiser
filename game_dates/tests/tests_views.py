from django.test import TestCase, Client
from django.urls import reverse, resolve
from game_dates.models import *
import json

'''
Tests run on sqllite database
'''


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('index')

    def test_index(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
