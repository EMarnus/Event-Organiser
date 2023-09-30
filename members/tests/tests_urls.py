from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import *


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_register_url_resolves(self):
        url = reverse('register_user')
        self.assertEquals(resolve(url).func, register_user)
