from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Player name")
    number = models.PositiveSmallIntegerField(verbose_name="Player number")
    country = models.CharField(max_length=50, verbose_name="Player country")
    type = models.CharField(
        max_length=50, verbose_name="Player type"
    )  # Todo add choices
    age = models.PositiveSmallIntegerField(verbose_name="Player age")
