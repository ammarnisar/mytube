# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Video, Likes, Channel, Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from .serializers import *
from django.contrib.auth.views import LoginView


# Create your views here.
# @login_required
def home(request):
    video = Video.objects.all()
    context = {
        'videos': video,
    }
    return render(request, 'index.html', context=context)


def videodetail(request, pk):
    video = Video.objects.get(pk=pk)
    video_most_likes = Video.objects.all().order_by("-likes").distinct()
    # video_most_likes=video_most_likes.filter(video.title)
    # video_most_likes = Video.objects.all().order_by("-likes").filter(video.id)
    video.views = video.views + 1
    video.save()

    # mostlikes(request , pk)
    is_liked = False
    like = video.likes.filter(user=request.user)
    print(like)
    if like:
        is_liked = True
    context = {
        'videos': video,
        'is_liked': is_liked,
        'video_most_likes':video_most_likes
    }
    return render(request, 'video-detail.html', context=context)


@api_view(['GET'])
def mostlikes(request):
    # video = Video.objects.get.all()
    # video = Video.objects.get(pk=pk)

    video_most_likes = Video.objects.all().order_by("-likescounts").distinct()
    serializer=VideoSerializer(video_most_likes,many=True)
    return Response(
        data=serializer.data,
        status=200
    )

def likes(request, pk):
    video = Video.objects.get(pk=pk)
    is_liked = False
    like = video.likes.filter(user=request.user)
    print(like)
    if like:
        like = like.first()
        print(like)
        video.likes.remove(like)
        video.likescounts = video.likescounts - 1;
        like.delete()

        is_liked = False
    else:
        like = Likes.objects.create(user=request.user)
        video.likescounts=video.likescounts + 1 ;
        video.likes.add(like)
        is_liked = True
    video.save()
    # url='video-detail/'+pk
    return redirect('video-detail', pk)


def add_comment(request, pk):
    # task = Task(status=pk)
    # task = Video.comments.objects.get(pk=pk)
    video = Video.objects.get(pk=pk)

    if request.method == 'POST':
        getcomment = request.POST.get('comment-user-message', '')
        cmt = Comment()
        cmt.comment = getcomment
        cmt.user = request.user
        cmt.save()
        video.comments.add(cmt)
        video.save()
        return redirect('home')
    else:
        print("fail")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            confirm_password = form.cleaned_data.get('password2')
            if raw_password == confirm_password:
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('home')

    else:
        form = SignUpForm()
    return redirect('home')


def customlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
        # Redirect to a success page.

    else:
        # Return an 'invalid login' error message.
        ...
    return HttpResponse('Error page')


def customlogout(request):
    logout(request)
    return redirect('home')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

# def password_validate(request):
#     passwordfirst = request.GET.get('password1', None)
#     confirm_password = request.GET.get('password2', None)
#
#     if passwordfirst == confirm_password:
#         return redirect('home')
#     else:
#         data = {
#             'is_taken': False
#         }
#     return JsonResponse(data)
