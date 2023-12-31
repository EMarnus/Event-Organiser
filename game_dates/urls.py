from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'booking',
        views.booking, name='booking'),
    path(
        'booking-submit',
        views.bookingSubmit, name='bookingSubmit'),
    path(
        'booking-details/<booking_id>',
        views.bookingDetails, name='bookingDetails'),
    path(
        'attending/<booking_id>/',
        views.attendingEvent, name='attending'),
    path(
        'tentative/<booking_id>/',
        views.tentativeEvent, name='tentative'),
    path(
        'booking-update/<booking_id>',
        views.bookingUpdate, name='bookingUpdate'),
    path(
        'booking-update-submit/<int:booking_id>',
        views.bookingUpdateSubmit, name='bookingUpdateSubmit'),
    path(
        'booking-delete/<booking_id>',
        views.bookingDelete, name='bookingDelete'),
    path(
        'user-panel',
        views.userPanel, name='userPanel'),
    path(
        'user-update/<int:id>',
        views.userUpdate, name='userUpdate'),

]
