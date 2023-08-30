from django import forms
from .models import Player
from .models import Team

class TeamForm(forms.ModelForm):
    team_name = forms.CharField()
    team_logo = forms.ImageField()
    manager_fname = forms.CharField()
    manager_lname = forms.CharField()
    manager_number = forms.IntegerField()
    manager_email = forms.EmailField()
    class Meta:
        model = Team
        fields = ['team_name', 'team_logo', 'manager_fname', 'manager_lname', 'manager_number', 'manager_email']
        
class PlayerForm(forms.ModelForm):
    player_fname = forms.CharField()
    player_lname = forms.CharField()
    player_age = forms.DateField()
    player_number = forms.IntegerField()
    player_email = forms.EmailField()
    player_image = forms.ImageField()
    class Meta:
        model = Player
        fields = ['player_fname','player_lname', 'player_age', 'player_number', 'player_email', 'player_image']
        

class PlayerBoxscore(forms.ModelForm):
    field_goals = forms.IntegerField()
    field_goals_percentage = forms.FloatField()
    three_pointers = forms.IntegerField()
    three_pointers_percentage = forms.FloatField()
    free_throws = forms.IntegerField()
    free_throws_percentage = forms.FloatField()
    rebounds = forms.IntegerField()
    assists = forms.IntegerField()
    steals = forms.IntegerField()
    blocks = forms.IntegerField()
    turnovers = forms.IntegerField()
    points = forms.IntegerField()