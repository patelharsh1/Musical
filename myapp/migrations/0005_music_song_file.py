# Generated by Django 5.0.3 on 2024-03-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_register_repassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='SONG_FILE',
            field=models.FileField(null=True, upload_to='songs'),
        ),
    ]
