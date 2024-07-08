from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newPerson", views.newPerson, name="newPerson"),
]
