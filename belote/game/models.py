from django.db import models


class Game(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    team_1 = models.ForeignKey("team.Team", on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.ForeignKey("team.Team", on_delete=models.CASCADE, related_name="team_2")

    team_1_score = models.IntegerField(default=0)
    team_2_score = models.IntegerField(default=0)

    winner = models.ForeignKey("team.Team", on_delete=models.CASCADE, related_name="winner", null=True, blank=True)

    def __str__(self):
        return f"{self.team_1} vs {self.team_2}"

    def is_full(self):
        return self.team_1.is_full() and self.team_2.is_full()

    def is_on_going(self):
        return self.ended_at is None

    def is_ended(self):
        return self.ended_at is not None


class Round(models.Model):
    game = models.ForeignKey("Game", related_name="rounds", on_delete=models.CASCADE)

    round_number = models.IntegerField(default=0)

    team_1_score = models.IntegerField(default=0)
    team_2_score = models.IntegerField(default=0)

    asset_card = models.ForeignKey("card.Card", on_delete=models.CASCADE, null=True, blank=True)
    asset_taker = models.ForeignKey("player.Player", related_name="rounds_as_asset_taker", on_delete=models.CASCADE, null=True, blank=True)

    dealer = models.ForeignKey("player.Player", related_name="rounds_as_dealer", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.team_1_score} vs {self.team_2_score}"

    def is_ended(self):
        return self.ended_at is not None


class CardPlayed(models.Model):
    round = models.ForeignKey("Round", on_delete=models.CASCADE, related_name="cards_played")
    player = models.ForeignKey("player.Player", on_delete=models.CASCADE, null=True, blank=True, related_name="cards_played")
    card = models.ForeignKey("card.Card", on_delete=models.CASCADE)
    play_order = models.IntegerField()

    won_fold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team} played {self.card}"
