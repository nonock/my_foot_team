from django.db import models
from django.utils.translation import gettext as _


class PenaltyStatMixin(models.Model):
    nbr_of_penalty_committed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty committed"), default=0
    )
    nbr_of_penalty_won = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty won"), default=0
    )
    nbr_of_penalty_scored = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty scored"), default=0
    )
    nbr_of_penalty_missed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty missed"), default=0
    )

    class Meta:
        abstract = True


class DribbleStatMixin(models.Model):
    nbr_of_dribble_attempts = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dribble attempts"), default=0
    )
    nbr_of_dribble_success = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dribble success"), default=0
    )

    class Meta:
        abstract = True


class DefensiveStatMixin(models.Model):
    nbr_of_tackles = models.PositiveSmallIntegerField(
        verbose_name=_("Number of tackles"), default=0
    )
    nbr_of_blocks = models.PositiveSmallIntegerField(
        verbose_name=_("Number of blocks"), default=0
    )
    nbr_of_interception = models.PositiveSmallIntegerField(
        verbose_name=_("Number of interception"), default=0
    )
    nbr_of_clearances = models.PositiveSmallIntegerField(
        verbose_name=_("Number of clearances"), default=0
    )
    nbr_of_dispossessed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dispossessed"), default=0
    )
    nbr_of_saves = models.PositiveSmallIntegerField(
        verbose_name=_("Number of saves"), default=0
    )
    nbr_of_inside_box_saves = models.PositiveSmallIntegerField(
        verbose_name=_("Number of inside box saves"), default=0
    )
    nbr_of_duels = models.PositiveSmallIntegerField(
        verbose_name=_("Number of duels"), default=0
    )
    nbr_of_duels_won = models.PositiveSmallIntegerField(
        verbose_name=_("Number of duels won"), default=0
    )

    class Meta:
        abstract = True


class PasseStatMixin(models.Model):
    nbr_of_crosses = models.PositiveSmallIntegerField(
        verbose_name=_("Number of crosses"), default=0
    )
    nbr_of_passes = models.PositiveSmallIntegerField(
        verbose_name=_("Number of passes"), default=0
    )
    passes_accuracy = models.FloatField(verbose_name=_("Passes accuracy"), default=0)
    nbr_of_key_passes = models.PositiveSmallIntegerField(
        verbose_name=_("Number of key passes"), default=0
    )

    class Meta:
        abstract = True


class AttackStatMixin(models.Model):
    nbr_of_goals = models.PositiveSmallIntegerField(
        verbose_name=_("Number of goals"), default=0
    )
    nbr_of_assists = models.PositiveSmallIntegerField(
        verbose_name=_("Number of assists"), default=0
    )
    nbr_of_shots = models.PositiveSmallIntegerField(
        verbose_name=_("Number of shots"), default=0
    )
    nbr_of_woodwork = models.PositiveSmallIntegerField(
        verbose_name=_("Number of woodwork"), default=0
    )

    class Meta:
        abstract = True


class PlayerStatMixin(
    PenaltyStatMixin,
    DribbleStatMixin,
    DefensiveStatMixin,
    PasseStatMixin,
    AttackStatMixin,
    models.Model,
):
    nbr_of_match_played = models.PositiveSmallIntegerField(
        verbose_name=_("Number of match played"), default=0
    )
    nbr_of_yellow_cards = models.PositiveSmallIntegerField(
        verbose_name=_("Number of yellow card"), default=0
    )
    nbr_of_red_cards = models.PositiveSmallIntegerField(
        verbose_name=_("Number of red cards"), default=0
    )
    nbr_of_minutes_played = models.PositiveSmallIntegerField(
        verbose_name=_("Number of minutes played"), default=0
    )
    is_injured = models.BooleanField(default=False, verbose_name=_("Is injured"))
    nbr_of_substitute_out = models.PositiveSmallIntegerField(
        verbose_name=_("Number of substitute out"), default=0
    )
    nbr_of_substitute_on_bench = models.PositiveSmallIntegerField(
        verbose_name=_("Number of substitute on bench"), default=0
    )
    is_captain = models.BooleanField(default=False, verbose_name=_("Is captain"))
    nbr_of_goals_conceded = models.PositiveSmallIntegerField(
        verbose_name=_("Number of goals conceded"), default=0
    )
    nbr_of_fouls_committed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of fouls committed"), default=0
    )
    rating = models.FloatField(verbose_name=_("Rating"), default=0)

    class Meta:
        abstract = True
