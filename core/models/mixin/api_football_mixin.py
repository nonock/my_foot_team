from django.db import models


class ApiFootBallMixin(models.Model):
    id_api_football = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True
