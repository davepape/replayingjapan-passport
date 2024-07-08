from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    context = {}
    name = request.session.get('name')
    if name:
        context['name'] = name
        return render(request, 'welcome.html', context)
    else:
        return render(request, 'register.html', context)


def newPerson(request):
    name = request.POST.get('yourname','')
    email = request.POST.get('youremail','')
    request.session['name'] = name
    request.session['email'] = email
    try:
        p = Player.objects.get(email=email)
    except Player.DoesNotExist:
        p = Player(name=name, email=email)
        p.save()
    context = { 'name': name }
    return render(request, 'welcome.html', context)


def visit(request,id):
    vp = get_object_or_404(VisitPoint,pk=id)
    email = request.session.get('email')
    if not email:
        return render(request, 'register.html', {})
    player = get_object_or_404(Player, email=email)
    try:
        visited = PlayerVisited.objects.get(player = player, visitPoint = vp)
    except PlayerVisited.DoesNotExist:
        visited = PlayerVisited(player = player, visitPoint = vp)
        visited.save()
    return HttpResponseRedirect(vp.url)

@login_required
def stats(request):
    playerData = []
    for p in Player.objects.all():
        pointData = []
        pv = PlayerVisited.objects.filter(player = p)
        for i in pv:
            pointData.append(i.visitPoint)
        playerData.append({'player':p, 'visitPoints':pointData})
    visitPointData = []
    for vp in VisitPoint.objects.all():
        visitorData = []
        pv = PlayerVisited.objects.filter(visitPoint = vp)
        for i in pv:
            visitorData.append(i.player)
        visitPointData.append({'visitPoint':vp, 'visitors': visitorData})
    tableData = []
    for p in playerData:
        rowData = [p['player'].name]
        for vp in visitPointData:
            if vp['visitPoint'] in p['visitPoints']:
                val = 'x'
            else:
                val = ' '
            rowData.append(val)
        tableData.append(rowData)
    context = { 'players': playerData, 'visitPoints': visitPointData, 'table': tableData }
    return render(request, 'stats.html', context)
