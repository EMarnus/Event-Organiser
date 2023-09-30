from django.test import SimpleTestCase
from django.urls import reverse, resolve
from game_dates.views import *


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_booking_url_resolves(self):
        url = reverse('booking')
        self.assertEquals(resolve(url).func, booking)

    def test_bookingSubmit_url_resolves(self):
        url = reverse('bookingSubmit')
        self.assertEquals(resolve(url).func, bookingSubmit)

    def test_bookingDetails_url_resolves(self):
        url = reverse('bookingDetails', args=[1])
        self.assertEquals(resolve(url).func, bookingDetails)

    def test_attending_url_resolves(self):
        url = reverse('attending', args=[1])
        self.assertEquals(resolve(url).func, attendingEvent)

    def test_tentative_url_resolves(self):
        url = reverse('tentative', args=[1])
        self.assertEquals(resolve(url).func, tentativeEvent)

    def test_bookingUpdate_url_resolves(self):
        url = reverse('bookingUpdate', args=[1])
        self.assertEquals(resolve(url).func, bookingUpdate)

    def test_bookingUpdateSubmit_url_resolves(self):
        url = reverse('bookingUpdateSubmit', args=[1])
        self.assertEquals(resolve(url).func, bookingUpdateSubmit)

    def test_bookingDelete_url_resolves(self):
        url = reverse('bookingDelete', args=[1])
        self.assertEquals(resolve(url).func, bookingDelete)

    def test_userPanel_url_resolves(self):
        url = reverse('userPanel')
        self.assertEquals(resolve(url).func, userPanel)

    def test_userUpdate_url_resolves(self):
        url = reverse('userUpdate', args=[1])
        self.assertEquals(resolve(url).func, userUpdate)
