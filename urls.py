from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("newPerson", views.newPerson, name="newPerson"),
    path("visit/<int:id>", views.visit, name="visit"),
    path("stats", views.stats, name="stats"),
    path("stats_admin", views.stats_admin, name="stats_admin"),
    path("visitpoints", views.visitpoints, name="visitpoints"),
]
