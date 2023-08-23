from django.contrib import admin
from .models import Team, Player, ScoreKeeper, Game

class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'team_name', 'team_logo', 'manager_fname', 'manager_lname', 'manager_number', 'manager_email', 'wins', 'loses']
    search_fields = ['team_name', 'manager_fname']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'player_fname', 'player_lname', 'player_age', 'player_number', 'player_email', 'player_image', 'team', 'field_goals', 'field_goals_percentage', 'three_pointers', 'three_pointers_percentage', 'free_throws', 'free_throws_percentage', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'points']
    search_fields = ['player_fname', 'team_name', 'player_number']

class ScoreKeeperAdmin(admin.ModelAdmin):
    list_display = ['keeper_id', 'keeper_name', 'keeper_number', 'keeper_email', 'keeper_username', 'keeper_password', 'game_id']
    search_fields = ['keeper_name', 'keeper_id', 'keeper_number']

class GameAdmin(admin.ModelAdmin):
    list_display = ['game_id', 'team_1_id', 'team_2_id', 'game_status', 'game_date', 'team_1_score', 'team_2_score']
    search_fields = ['game_id', 'team_1_id__team_name', 'team_2_id__team_name']

# class AdminAdmin(admin.ModelAdmin):
#     list_display = ['admin_id', 'admin_name', 'admin_email', 'admin_username', 'admin_email', 'admin_password']
#     search_fields = ['admin_name', 'admin_username']

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(ScoreKeeper, ScoreKeeperAdmin)
admin.site.register(Game, GameAdmin)
# admin.site.register(Admin, AdminAdmin)
