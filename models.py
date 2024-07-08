from django.db import models

class VisitPoint(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class PlayerVisited(models.Model):
    player = models.ForeignKey(Player)
    visitPoint = models.ForeignKey(VisitPoint)

