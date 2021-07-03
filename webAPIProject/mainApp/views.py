from django.shortcuts import render
from .models import *

# Create your views here.

def main(request):
    cafes = Cafe.objects.all()
    return render(request, 'main.html', {'cafes': cafes})