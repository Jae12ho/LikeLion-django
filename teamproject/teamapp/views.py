from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    blogs = Blog.objects.all() #blog 테이블의 모든 오브젝트 불러오기
    teams = Team.objects.all()
    return render(request, 'home.html', {'blogs' : blogs, 'teams' : teams}) #html, blogs 보내주기