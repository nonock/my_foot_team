from django.db import models
from django.utils.translation import gettext as _

from core.models.mixin import ApiFootBallMixin


class League(ApiFootBallMixin):
    name = models.CharField(max_length=200, verbose_name=_("League name"))
    logo = models.CharField(max_length=200, verbose_name=_("League logo"))
    country = models.ForeignKey("core.Country", on_delete=models.CASCADE)
    season = models.CharField(max_length=200, verbose_name=_("League season"))
