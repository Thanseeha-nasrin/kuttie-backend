from django.db import models

class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.points} pts"

