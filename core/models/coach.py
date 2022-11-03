from django.db import models
from django.utils.translation import gettext as _


class Coach(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Coach name"))
    country = models.ForeignKey("core.Country", on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name=_("Coach age"))
    team = models.ForeignKey(
        "core.Team",
        on_delete=models.CASCADE,
        verbose_name=_("Team"),
        null=True,
        blank=True,
    )
