from django.contrib import admin

from core.models import Coach, Country, League, Player, Team

admin.site.register(Player)
admin.site.register(Country)
admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(League)
