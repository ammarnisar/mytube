from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('video-detail/<int:pk>', views.videodetail, name='video-detail'),
    path('mostlikes', views.mostlikes, name='video-most-likes'),
    path('add_comment/<int:pk>', views.add_comment, name='add_comment'),
    path('signupform',views.signup, name='Signupform'),
    path('login' , views.customlogin, name='login'),
    path('logout',views.customlogout,name='logout'),
    path('validate_username',views.validate_username,name='validate_username'),
    path('likes/<int:pk>', views.likes, name='likes')
    # path('password_validate', views.password_validate, name='password_validate')

    # path('login', include('django.contrib.auth.urls'))
]