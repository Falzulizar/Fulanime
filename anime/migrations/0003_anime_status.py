# Generated by Django 4.2.7 on 2023-11-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_trendinganime_recommendedanime'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing', max_length=20),
        ),
    ]
