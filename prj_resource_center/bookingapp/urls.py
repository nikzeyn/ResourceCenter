from django.urls import path
from bookingapp import views


urlpatterns = [ 
	path('', views.BookingHome.as_view() , name='booking_home'),

]
