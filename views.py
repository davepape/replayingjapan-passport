from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    x = request.session.get('name','unknown')
    request.session['name'] = "Dave"
    return HttpResponse("Hello, " + x + ". You're at the test index.")
