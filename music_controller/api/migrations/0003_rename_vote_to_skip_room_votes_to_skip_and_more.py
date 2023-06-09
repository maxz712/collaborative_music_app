# Generated by Django 4.2.1 on 2023-06-09 01:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_votes_to_skip_room_vote_to_skip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='vote_to_skip',
            new_name='votes_to_skip',
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]