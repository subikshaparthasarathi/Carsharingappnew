from django.urls import path,include
from django.urls import re_path as url
from home.views import *
from car_dealer_portal import *
from customer_portal import *

urlpatterns = [
    url(r'^$',home_page),
]
