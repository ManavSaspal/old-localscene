from django.urls import path 
from . import views 

urlpatterns = [
    path('event/',views.event_page),
    path('login/', views.login)
]