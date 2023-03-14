from django.urls import path 
from . import views 

urlpatterns = [
    path('hello/',views.event_page),
    path('login/',views.login)
]