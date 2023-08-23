from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PlayerForm, TeamForm
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


# {'team_name': 'AMB', 'team_logo': <InMemoryUploadedFile: corporate.png (image/png)>, 'manager_fname': 'Sulaiman', 'manager_lname': 'AbuQamar', 'manager_number': 562914945, 'manager_email': 'sabuqamar82@gmail.com', 'player_fname': 'Sulaiman', 'player_lname': 'AbuQamar', 'player_number': 562914945, 'player_email': 'sabuqamar82@gmail.com'}

from django.shortcuts import render, redirect
from .forms import TeamForm, PlayerForm

def register(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        player_form = PlayerForm(request.POST, request.FILES)
        
        # if team_form.is_valid() and player_form.is_valid():
        team = team_form.save()
        player = player_form.save(commit=False)
        player.team_id = team
        player.save()
        return redirect('schedule.html')
            
    else:
        team_form = TeamForm()
        player_form = PlayerForm()
        
    context = {
        'team_form': team_form,
        'player_form': player_form,
    }
    
    return render(request, 'register.html', context)



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