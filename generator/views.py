from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def h2(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = int(request.GET.get('length'))
    if request.GET.get('uc'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('nu'):
        char.extend(list('123456789'))
    if request.GET.get('sc'):
        char.extend(list('!@#$%^&*'))
    for x in range(length):
           password += random.choice(char)
    return render(request,'generator/pass.html',{'gen':password})

def h3(request):
    return render(request,'generator/about.html')