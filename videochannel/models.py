# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes_datetime = models.DateTimeField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return  str(self.user)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=500 , null=False, blank=False ,default='')
    comment_name=models.CharField(max_length=50,null=False, blank=False ,default='')
    comment_email=models.EmailField(null=False, blank=False, default='')
    comment_datetime = models.DateTimeField(null=False, blank=False,auto_now_add=True)

    def __str__(self):
        return self.comment


class Video(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    views = models.PositiveIntegerField(null=False, default=0)
    video_url = models.CharField(null=False, blank=False, max_length=200)
    title = models.CharField(null=False, blank=False, max_length=40)
    description = models.TextField(null=False, blank=False)
    likes = models.ManyToManyField(Likes, related_name='likes',null=True ,blank=True , default=0)
    likescounts=models.PositiveIntegerField(null=False, default=0)
    comments = models.ManyToManyField(Comment, null=True , blank=True)
    datetime = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title



class Channel(models.Model):
    title=models.CharField(null=False,blank=False ,max_length=60)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    videos=models.ManyToManyField(Video)
    subcriber = models.ManyToManyField(User, related_name='subcriber')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()