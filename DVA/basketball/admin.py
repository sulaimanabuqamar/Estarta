from django.contrib import admin
from .models import Team, Player, ScoreKeeper, Game, Admin

class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'manager_fname', 'manager_lname', 'wins', 'loses']
    search_fields = ['team_name', 'manager_fname']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'player_fname', 'player_lname', 'player_age', 'player_number']
    search_fields = ['player_fname', 'team_name', 'player_number']

class ScoreKeeperAdmin(admin.ModelAdmin):
    list_display = ['keeper_id', 'keeper_name', 'game_id']
    search_fields = ['keeper_name', 'game_id__team_1_id__team_name', 'game_id__team_2_id__team_name']

class GameAdmin(admin.ModelAdmin):
    list_display = ['game_id', 'team_1_id', 'team_2_id', 'game_status', 'game_date']
    search_fields = ['game_id', 'team_1_id__team_name', 'team_2_id__team_name']

class AdminAdmin(admin.ModelAdmin):
    list_display = ['admin_id', 'admin_name', 'admin_email', 'admin_username']
    search_fields = ['admin_name', 'admin_username']

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(ScoreKeeper, ScoreKeeperAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Admin, AdminAdmin)
