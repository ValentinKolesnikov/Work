from django.shortcuts import render
from event.models import Event

def index(request):
    events = Event.objects.all()
    topevent = events.order_by("-mark")[0]
    start = len(events)
    massiv1 = events[start-3 if start>2 else 0:start]
    massiv2 = events[start-4 if start>3 else 0:start]
    
    return render(request, 'mainApp/homePage.html', {'news':massiv1,'bar':massiv2, 'top':topevent})