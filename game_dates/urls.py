from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('booking-details/<booking_id>', views.bookingDetails, name='bookingDetails'),
    path('booking-update/<booking_id>', views.bookingUpdate, name='bookingUpdate'),
    path('booking-update-submit/<int:booking_id>', views.bookingUpdateSubmit, name='bookingUpdateSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    #path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    #path('organiser-panel', views.organiserPanel, name='organiserPanel'),
]
