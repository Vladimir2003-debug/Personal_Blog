# Generated by Django 4.2.3 on 2023-07-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_album_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True),
        ),
    ]