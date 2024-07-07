from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'register.html', context)

def newperson(request):
    name = request.POST.get('yourname','')
    email = request.POST.get('youremail','')
    request.session['name'] = name
    context = { 'name': name }
    return render(request, 'welcome.html', context)

