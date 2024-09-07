from django.shortcuts import render
from services.models import Service

def home(request):
    services = Service.objects.all().order_by('-id')[:3]  # последние 3 услуги
    return render(request, 'home.html', {'services': services})
