from django.db import models
from django.utils.translation import gettext as _

from core.models.mixin import ApiFootBallMixin, PlayerStatMixin


class Player(ApiFootBallMixin, PlayerStatMixin):
    name = models.CharField(max_length=200, verbose_name=_("Player name"))
    logo = models.CharField(max_length=200, verbose_name=_("Player image"))
    number = models.PositiveSmallIntegerField(verbose_name=_("Player number"))
    country = models.ForeignKey(
        "core.Country", on_delete=models.CASCADE, blank=True, null=True
    )
    type = models.CharField(
        max_length=50, verbose_name=_("Player type")
    )  # Todo add choices
    age = models.PositiveSmallIntegerField(verbose_name=_("Player age"))
    team = models.ForeignKey(
        "core.Team",
        on_delete=models.CASCADE,
        verbose_name=_("Team"),
        blank=True,
        null=True,
    )
