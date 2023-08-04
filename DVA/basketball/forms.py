from django import forms


class PlayerForm(forms.Form):
    player_fname = forms.CharField()