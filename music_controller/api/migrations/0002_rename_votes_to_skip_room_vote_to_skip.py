# Generated by Django 4.2.1 on 2023-05-28 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='votes_to_skip',
            new_name='vote_to_skip',
        ),
    ]
