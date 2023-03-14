from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def event_page(request):
    event_title = "one8 Run, Bengaluru"
    event_description = "one8 is a brand of Virat Kohli that celebrates his philosophies and way of life. one8 is elated to announce the first edition of its run in the following categories - 5km, 10km, 18km Join Virat Kohli and witness a running revolution. The amount paid includes the registration cost, T-Shirt, Timing Chip (based on the race category), E-certificate, Medal, Breakfast and race support.."
    event_date = "March 26"
    event_time = "7:00 AM - 9:00 AM"
    event_venue = "Nice Tollgate Hosakerehalli, Bengaluru"
    
    context = {
        'event_title': event_title,
        'event_description': event_description,
        'event_date': event_date,
        'event_time': event_time,
        'event_venue': event_venue,
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