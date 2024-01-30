from django.db import models


class Team(models.Model):
    game = models.ForeignKey("game.Game", on_delete=models.CASCADE)

    player_1 = models.ForeignKey("player.Player", on_delete=models.CASCADE, related_name="player_1")
    player_2 = models.ForeignKey("player.Player", on_delete=models.CASCADE, related_name="player_2")
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player_1} and {self.player_2}"
