# Generated by Django 2.2.1 on 2019-07-22 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videochannel', '0020_video_likescounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='likescounts',
        ),
    ]
