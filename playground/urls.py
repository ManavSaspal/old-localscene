from django.urls import path 
from . import views 
from playground.models import *

urlpatterns = [
    path('login/', views.login)
]

for obj in Event.objects.all():
    urlpatterns.append(path(obj.slug, views.event_page))

