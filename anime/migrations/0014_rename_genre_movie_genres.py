# Generated by Django 4.1.5 on 2024-03-06 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0013_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
    ]
