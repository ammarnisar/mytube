# Generated by Django 2.2.1 on 2019-05-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochannel', '0003_auto_20190504_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='like',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
