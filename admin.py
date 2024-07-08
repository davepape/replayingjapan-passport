from django.contrib import admin

from .models import VisitPoint, Player, PlayerVisited
admin.site.register(VisitPoint)
admin.site.register(Player)
admin.site.register(PlayerVisited)
