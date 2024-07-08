from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    context = {}
    return render(request, 'register.html', context)

def newPerson(request):
    name = request.POST.get('yourname','')
    email = request.POST.get('youremail','')
    request.session['name'] = name
    try:
        p = Player.objects.get(name=name)
    except Player.DoesNotExist:
        p = Player(name=name, email=email)
        p.save()
    context = { 'name': name }
    return render(request, 'welcome.html', context)

