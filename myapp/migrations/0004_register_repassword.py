# Generated by Django 5.0.3 on 2024-03-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_playlist_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='repassword',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
