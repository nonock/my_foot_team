from django.db import models
from django.utils.translation import gettext as _

from core.models.mixin import ApiFootBallMixin


class Team(ApiFootBallMixin):
    name = models.CharField(max_length=200, verbose_name=_("Team name"))
    logo = models.CharField(max_length=200, verbose_name=_("Team logo"))
