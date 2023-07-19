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
    path("schedule/boxscore/", views.boxScore, name="boxscore"),
    path("stats/allstats", views.allStats, name="allstats"),
    path("admin/login/", views.login, name="login"),
    path("admin/schedule/", views.adminSchedule, name="admin_schedule"),
    path("admin/schedule/boxscore/", views.boxScore, name="boxscore"),
    path("admin/register/", views.adminRegister, name="admin_register"),
    path("admin/register/team/", views.adminRegister2, name="admin_register2"),
    path("admin/teams/", views.adminTeams, name="admin_teams"),
    path("admin/accounts/", views.adminAccounts, name="admin_accounts"),
    path("admin/accounts/user/", views.adminAccounts2, name="admin_accounts2"),
]