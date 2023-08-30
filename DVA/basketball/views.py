from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PlayerForm, TeamForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "LandingPage.html")

def schedule(request):
    model_data = Game.objects.all()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return render(request, "Schedule.html", {'schedule': model_data, 'months': months})

def teams(request):
    model_data = Team.objects.all()
    return render(request, "Teams.html", {'teams': model_data})

def stats(request):
    point_leaders = Player.objects.order_by('-points')[:5]
    assist_leaders = Player.objects.order_by('-assists')[:5]
    rebound_leaders = Player.objects.order_by('-rebounds')[:5]
    block_leaders = Player.objects.order_by('-blocks')[:5]
    steal_leaders = Player.objects.order_by('-steals')[:5]
    three_pointers_leaders = Player.objects.order_by('-three_pointers')[:5] 
    
    context = {
        'point_leaders': point_leaders,
        'assist_leaders': assist_leaders,
        'rebound_leaders': rebound_leaders,
        'assist_leaders': block_leaders,
        'steal_leaders': steal_leaders,
        'three_pointers_leaders': three_pointers_leaders,
    }

    return render(request, "Stats.html", context)


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

def boxScore(request, game_id):
    game = Game.objects.get(pk=game_id)
    
    team1_players = Player.objects.filter(team_id=game.team_1_id)
    team2_players = Player.objects.filter(team_id=game.team_2_id)
    
    context = {
        'team1_players': team1_players,
        'team2_players': team2_players,
        'team1_name': game.team_1_id.team_name,
        'team2_name': game.team_2_id.team_name,
    }
    
    return render(request, "Boxscore.html", context)

# def savePlayerStats(request, game_id):
#     game = Game.objects.get(pk=game_id)
    
#     team1_players = Player.objects.filter(team_id=game.team_1_id)
#     team2_players = Player.objects.filter(team_id=game.team_2_id)
    
#     context = {
#         'game': game,
#         'team1_players': team1_players,
#         'team2_players': team2_players,
#         'team1_name': game.team_1_id.team_name,
#         'team2_name': game.team_2_id.team_name,
#     }
    
#     if request.method == 'POST':
#         Playerstats = PlayerBoxscore(request.POST)
        
#         if Playerstats.is_valid():
#             Playerstats.save()
#             return redirect('boxscore', game_id=game_id)  
#     return render(request, "Boxscore.html", context)


def allStats(request):
    return render(request, "AllStats.html")

def login(request):
    return render(request, "Login.html")