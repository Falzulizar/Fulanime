# Generated by Django 4.1.5 on 2024-03-06 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0016_comment_dislikes_comment_likes_comment_reply_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
    ]
