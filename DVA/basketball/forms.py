from django import forms
from .models import Player
from .models import Team

class TeamForm(forms.ModelForm):
    team_id = forms.CharField(max_length=15)
    team_name = forms.CharField(max_length=25)
    team_logo = forms.ImageField()
    manager_fname = forms.CharField(max_length=25)
    manager_lname = forms.CharField(max_length=25)
    manager_number = forms.IntegerField()
    manager_email = forms.EmailField(max_length=25)
    class Meta:
        model = Team
        fields = ['team_id','team_name', 'team_logo', 'manager_fname', 'manager_lname', 'manager_number', 'manager_email']
        
class PlayerForm(forms.ModelForm):
    player_fname = forms.CharField()
    player_lname = forms.CharField(max_length=25)
    player_age = forms.IntegerField()
    player_number = forms.IntegerField()
    player_email = forms.EmailField(max_length=25)
    player_image = forms.ImageField()
    team_id = forms.CharField(max_length=15)
    class Meta:
        model = Player
        fields = ['player_fname','player_lname', 'player_age', 'player_number', 'player_email', 'player_image', 'team_id']

class RegisterationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        self.fields['team_id'] = TeamForm().fields['team_id']
        self.fields['team_name'] = TeamForm().fields['team_name']
        self.fields['team_logo'] = TeamForm().fields['team_logo']
        self.fields['manager_fname'] = TeamForm().fields['manager_fname']
        self.fields['manager_lname'] = TeamForm().fields['manager_lname']
        self.fields['manager_number'] = TeamForm().fields['manager_number']
        self.fields['manager_email'] = TeamForm().fields['manager_email']
        self.fields['player_fname'] = PlayerForm().fields['player_fname']
        self.fields['player_lname'] = PlayerForm().fields['player_lname']
        self.fields['player_age'] = PlayerForm().fields['player_age']
        self.fields['player_number'] = PlayerForm().fields['player_number']
        self.fields['player_email'] = PlayerForm().fields['player_email']
        self.fields['player_image'] = PlayerForm().fields['player_image']
