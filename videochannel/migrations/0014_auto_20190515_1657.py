# Generated by Django 2.2.1 on 2019-05-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochannel', '0013_auto_20190515_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='videochannel.Likes'),
        ),
    ]
