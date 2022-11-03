from django.db import models
from django.utils.translation import gettext as _

from core.models.mixin import ApiFootBallMixin


class Country(ApiFootBallMixin):
    name = models.CharField(max_length=200, verbose_name=_("Country name"), unique=True)
    logo = models.CharField(max_length=200, verbose_name=_("Country flag"))
