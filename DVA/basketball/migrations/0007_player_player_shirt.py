# Generated by Django 4.2.3 on 2023-08-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basketball", "0006_player_field_goals_percentage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="player_shirt",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
