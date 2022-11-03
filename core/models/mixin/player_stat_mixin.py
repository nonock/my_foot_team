from django.db import models
from django.utils.translation import gettext as _


class PenaltyStatMixin(models.Model):
    nbr_of_penalty_committed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty committed")
    )
    nbr_of_penalty_won = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty won")
    )
    nbr_of_penalty_scored = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty scored")
    )
    nbr_of_penalty_missed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of penalty missed")
    )

    class Meta:
        abstract = True


class DribbleStatMixin(models.Model):
    nbr_of_dribble_attempts = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dribble attempts")
    )
    nbr_of_dribble_success = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dribble success")
    )

    class Meta:
        abstract = True


class DefensiveStatMixin(models.Model):
    nbr_of_tackles = models.PositiveSmallIntegerField(
        verbose_name=_("Number of tackles")
    )
    nbr_of_blocks = models.PositiveSmallIntegerField(verbose_name=_("Number of blocks"))
    nbr_of_interception = models.PositiveSmallIntegerField(
        verbose_name=_("Number of interception")
    )
    nbr_of_clearances = models.PositiveSmallIntegerField(
        verbose_name=_("Number of clearances")
    )
    nbr_of_dispossessed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of dispossessed")
    )
    nbr_of_saves = models.PositiveSmallIntegerField(verbose_name=_("Number of saves"))
    nbr_of_inside_box_saves = models.PositiveSmallIntegerField(
        verbose_name=_("Number of inside box saves")
    )
    nbr_of_duels = models.PositiveSmallIntegerField(verbose_name=_("Number of duels"))
    nbr_of_duels_won = models.PositiveSmallIntegerField(
        verbose_name=_("Number of duels won")
    )

    class Meta:
        abstract = True


class PasseStatMixin(models.Model):
    nbr_of_crosses = models.PositiveSmallIntegerField(
        verbose_name=_("Number of crosses")
    )
    nbr_of_passes = models.PositiveSmallIntegerField(verbose_name=_("Number of passes"))
    passes_accuracy = models.FloatField(verbose_name=_("Passes accuracy"))
    nbr_of_key_passes = models.PositiveSmallIntegerField(
        verbose_name=_("Number of key passes")
    )

    class Meta:
        abstract = True


class AttackStatMixin(models.Model):
    nbr_of_goals = models.PositiveSmallIntegerField(verbose_name=_("Number of goals"))
    nbr_of_assists = models.PositiveSmallIntegerField(
        verbose_name=_("Number of assists")
    )
    nbr_of_shots = models.PositiveSmallIntegerField(verbose_name=_("Number of shots"))
    nbr_of_woodwork = models.PositiveSmallIntegerField(
        verbose_name=_("Number of woodwork")
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
        verbose_name=_("Number of match played")
    )
    nbr_of_yellow_cards = models.PositiveSmallIntegerField(
        verbose_name=_("Number of yellow card")
    )
    nbr_of_red_cards = models.PositiveSmallIntegerField(
        verbose_name=_("Number of red cards")
    )
    nbr_of_minutes_played = models.PositiveSmallIntegerField(
        verbose_name=_("Number of minutes played")
    )
    is_injured = models.BooleanField(default=False, verbose_name=_("Is injured"))
    nbr_of_substitute_out = models.PositiveSmallIntegerField(
        verbose_name=_("Number of substitute out")
    )
    nbr_of_substitute_on_bench = models.PositiveSmallIntegerField(
        verbose_name=_("Number of substitute on bench")
    )
    is_captain = models.BooleanField(default=False, verbose_name=_("Is captain"))
    nbr_of_goals_conceded = models.PositiveSmallIntegerField(
        verbose_name=_("Number of goals conceded")
    )
    nbr_of_fouls_committed = models.PositiveSmallIntegerField(
        verbose_name=_("Number of fouls committed")
    )
    rating = models.FloatField(verbose_name=_("Rating"))

    class Meta:
        abstract = True
