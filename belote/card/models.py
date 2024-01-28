from django.db import models


# Create your models here.
class Card(models.Model):
    class Suit(models.TextChoices):
        HEART = "Heart"
        CLUB = "Club"
        SPADE = "Spade"
        DIAMOND = "Diamond"

    class Rank(models.TextChoices):
        SEVEN = "7"
        EIGHT = "8"
        NINE = "9"
        TEN = "10"
        JACK = "Jack"
        QUEEN = "Queen"
        KING = "King"
        ACE = "Ace"

    suit = models.CharField(max_length=10, choices=Suit)
    rank = models.CharField(max_length=5, choices=Rank)
    value = models.IntegerField()
