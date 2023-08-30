from django.urls import path
from basketball import views
from templates import *

urlpatterns = [
    path("", views.home, name="home"),
    path("schedule/", views.schedule, name="schedule"),
    path("teams/", views.teams, name="teams"),
    path("stats/", views.stats, name="stats"),
    path("register/", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("schedule/boxscore/<int:game_id>/", views.boxScore, name="boxscore"),
    # path("schedule/boxscore/<int:game_id>/save/", views.savePlayerStats, name="save_player_stats"),
    path("stats/allstats", views.allStats, name="allstats"),
    path("login/", views.login, name="login"),
]