from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from playground.models import *


def event_page(request):
    request_slug = request.path[12:]
    e = Event.objects.get(slug = request_slug)
    event_name = e.name
    event_description = e.description
    event_time = e.startTime
    event_state = e.state
    event_venue = e.venue
    event_image = e.image
    
    context = {
        'event_name': event_name,
        'event_description': event_description,
        'event_time': event_time,
        'event_state': event_state,
        'event_venue': event_venue,
        'event_image': event_image 
    }
    
    return render(request, 'event_page.html', context)

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'login_page.html', {'form': form})