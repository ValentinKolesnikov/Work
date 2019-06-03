from django.shortcuts import render
from work.models import Work

def index(request):
    works = Work.objects.all()
    if len(works)==0:
        return render(request, 'mainApp/homePage.html', {})

    topwork = works.order_by("-mark")[0]
    start = len(works)
    massiv1 = works[start-3 if start>2 else 0:start]
    massiv2 = works[start-4 if start>3 else 0:start]
    
    return render(request, 'mainApp/homePage.html', {'news':massiv1,'bar':massiv2, 'top':topwork})

