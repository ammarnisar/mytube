# Generated by Django 2.2.1 on 2019-05-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochannel', '0015_auto_20190515_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_name',
            field=models.TextField(default=''),
        ),
    ]
