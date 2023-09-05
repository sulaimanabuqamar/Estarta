from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=40)
    team_abbreviation = models.CharField(max_length=4, default='DVA')
    team_logo = models.ImageField(upload_to='team_logos/')
    manager_fname = models.CharField(max_length=25)
    manager_lname = models.CharField(max_length=25)
    manager_number = models.IntegerField()
    manager_email = models.EmailField()
    wins = models.IntegerField(null=True, blank=True, default=0)
    loses = models.IntegerField(null=True, blank=True, default=0)
    
def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Game date must be today or later.")
 
class Game(models.Model):
    GAME_STATUS_CHOICES = [
        ('soon', 'Soon'),
        ('q1', 'Quarter 1'),
        ('q2', 'Quarter 2'),
        ('halftime', 'Halftime'),
        ('q3', 'Quarter 3'),
        ('q4', 'Quarter 4'),
        ('final', 'Final'),
    ]

    game_id = models.AutoField(primary_key=True)
    team_1_id = models.ForeignKey(Team, related_name='team_1_games', on_delete=models.CASCADE)
    team_2_id = models.ForeignKey(Team, related_name='team_2_games', on_delete=models.CASCADE)
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()
    game_status = models.CharField(max_length=20, choices=GAME_STATUS_CHOICES, default='Soon')
    game_date = models.DateField(validators=[validate_future_date])

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_fname = models.CharField(max_length=25)
    player_lname = models.CharField(max_length=25)
    player_age = models.DateField()
    player_number = models.IntegerField()
    player_email = models.EmailField(max_length=25)
    player_image = models.ImageField(upload_to='player_images/')
    player_shirt = models.IntegerField(null=True, blank=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    field_goals = models.IntegerField(null=True, blank=True, default=0)
    field_goals_percentage = models.FloatField(null=True, blank=True, default=0)
    three_pointers = models.IntegerField(null=True, blank=True, default=0)
    three_pointers_percentage = models.FloatField(null=True, blank=True, default=0)
    free_throws = models.IntegerField(null=True, blank=True, default=0)
    free_throws_percentage = models.FloatField(null=True, blank=True, default=0)
    rebounds = models.IntegerField(null=True, blank=True, default=0)
    assists = models.IntegerField(null=True, blank=True, default=0)
    steals = models.IntegerField(null=True, blank=True, default=0)
    blocks = models.IntegerField(null=True, blank=True, default=0)
    turnovers = models.IntegerField(null=True, blank=True, default=0)
    points = models.IntegerField(null=True, blank=True, default=0)
    games = models.ManyToManyField(Game, through='PlayerPerformance')

class ScoreKeeper(models.Model):
    keeper_id = models.AutoField(primary_key=True)
    keeper_name = models.CharField(max_length=25)
    keeper_number = models.BigIntegerField()
    keeper_email = models.EmailField(max_length=25)
    keeper_username = models.CharField(max_length=25)
    keeper_password = models.CharField(max_length=50) 
    game_id = models.ForeignKey('Game', on_delete=models.CASCADE)

class PlayerPerformance(models.Model):
    performance_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    field_goals = models.IntegerField(null=True, blank=True, default=0)
    three_pointers = models.IntegerField(null=True, blank=True, default=0)
    free_throws = models.IntegerField(null=True, blank=True, default=0)
    rebounds = models.IntegerField(null=True, blank=True, default=0)
    assists = models.IntegerField(null=True, blank=True, default=0)
    steals = models.IntegerField(null=True, blank=True, default=0)
    blocks = models.IntegerField(null=True, blank=True, default=0)
    turnovers = models.IntegerField(null=True, blank=True, default=0)
    points = models.IntegerField(null=True, blank=True, default=0)
