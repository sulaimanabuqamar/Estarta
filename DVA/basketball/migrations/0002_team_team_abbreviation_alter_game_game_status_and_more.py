# Generated by Django 4.2.3 on 2023-08-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basketball", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="team_abbreviation",
            field=models.CharField(default="DVA", max_length=4),
        ),
        migrations.AlterField(
            model_name="game",
            name="game_status",
            field=models.CharField(
                choices=[
                    ("q1", "Quarter 1"),
                    ("q2", "Quarter 2"),
                    ("halftime", "Halftime"),
                    ("q3", "Quarter 3"),
                    ("q4", "Quarter 4"),
                    ("final", "Final"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="team_name",
            field=models.CharField(max_length=40),
        ),
    ]
