from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegisterationForm, PlayerForm, TeamForm
from .models import *

# Create your views here.

def home(request):
    return render(request, "LandingPage.html")

def schedule(request):
    return render(request, "Schedule.html")

def teams(request):
    return render(request, "Teams.html")

def stats(request):
    return render(request, "Stats.html")

def register(request):
    if request.POST:
        form = RegisterationForm(request.POST, request.FILES)
        print(request.FILES)
        print(form)
        # form.save()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            team_name = cleaned_data['team_name']
            team_logo = cleaned_data['team_logo']
            manager_fname = cleaned_data['manager_fname']
            manager_lname = cleaned_data['manager_lname']
            manager_number = cleaned_data['manager_number']
            manager_email = cleaned_data['manager_email']
            player_fname = cleaned_data['player_fname']
            player_lname = cleaned_data['player_lname']
            player_age = cleaned_data['player_age']
            player_number = cleaned_data['player_number']
            player_email = cleaned_data['player_email']
            player_image = cleaned_data['player_image']
            team = Team(team_name = team_name, team_logo = team_logo, manager_fname = manager_fname, manager_lname = manager_lname, manager_number = manager_number, manager_email = manager_email)
            player = Player(player_fname = player_fname, player_lname = player_lname, player_age = player_age, player_number = player_number, player_email = player_email, player_image = player_image)
            team.save()
            player.save() 
        return redirect(schedule)
    return render(request, "Register.html", {'form' : RegisterationForm})

def about(request):
    return render(request, "About.html")

def boxScore(request):
    return render(request, "Boxscore.html")

def allStats(request):
    return render(request, "AllStats.html")

def login(request):
    return render(request, "Login.html")

def adminSchedule(request):
    return render(request, "Admin_Schedule.html")

def adminRegister(request):
    return render(request, "Admin_Register.html")

def adminTeams(request):
    return render(request, "Admin_Teams.html")

def adminTeams2(request):
    return render(request, "Admin_Register2.html")

def adminAccounts(request):
    return render(request, "Admin_Accounts.html")

def adminRegister2(request):
    return render(request, "Admin_Register2.html")

def adminAccounts2(request):
    return render(request, "Admin_Accounts2.html")