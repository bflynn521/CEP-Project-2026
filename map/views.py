from django.shortcuts import render
from .models import User

def campus_map_view(request):
    return render(request, 'campus_map.html')

def carpooling_view(request):
    users = User.objects.all()
    return render(request, 'carpooling.html', {'users': users})