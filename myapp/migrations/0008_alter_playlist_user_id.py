# Generated by Django 5.0.3 on 2024-03-09 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_playlist_song_id_alter_playlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='USER_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
    ]
