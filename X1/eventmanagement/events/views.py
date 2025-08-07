from django.shortcuts import render

# Create your views here.
from .models import Events

def home(request):
    return render(request , 'home.html')

def up_events(request):
    query = request.GET.get('eventname')
    if query:
        events = Events.objects.filter(eventname__icontains = query).order_by('eventdate')
    else:
        events = Events.objects.all().order_by('eventdate')
    return render(request , 'upcoming.html' , {'events':events})