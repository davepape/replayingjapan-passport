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
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    visitPoint = models.ForeignKey(VisitPoint, on_delete=models.PROTECT)
    def __str__(self):
        return self.player.name + ': ' + str(self.visitPoint.id)

