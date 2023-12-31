# Generated by Django 4.2.3 on 2023-08-31 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("basketball", "0004_remove_game_score_keeper"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="field_goals_percentage",
        ),
        migrations.RemoveField(
            model_name="player",
            name="free_throws_percentage",
        ),
        migrations.RemoveField(
            model_name="player",
            name="three_pointers_percentage",
        ),
        migrations.CreateModel(
            name="PlayerPerformance",
            fields=[
                ("performance_id", models.AutoField(primary_key=True, serialize=False)),
                ("field_goals", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "three_pointers",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("free_throws", models.IntegerField(blank=True, default=0, null=True)),
                ("rebounds", models.IntegerField(blank=True, default=0, null=True)),
                ("assists", models.IntegerField(blank=True, default=0, null=True)),
                ("steals", models.IntegerField(blank=True, default=0, null=True)),
                ("blocks", models.IntegerField(blank=True, default=0, null=True)),
                ("turnovers", models.IntegerField(blank=True, default=0, null=True)),
                ("points", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basketball.game",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basketball.player",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="games",
            field=models.ManyToManyField(
                through="basketball.PlayerPerformance", to="basketball.game"
            ),
        ),
    ]
