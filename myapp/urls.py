from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index3.html',views.index3page,name='index3'),
    path('index.html',views.indexpage,name='index'),
    path('',views.index2page,name='index2'),
    path('favourite.html',views.favouritepage,name='favourite'),
    path('pricing_plan.html',views.pricing_plan,name='pricing_plan'),
    path('add_playlist.html',views.add_playlist,name='add_playlist'),
    path('free_music.html',views.free_music,name='free_music'),
    path('genres_single.html',views.genres_single,name='genres_single'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logout,name='logout'),
    path('artistregister.html',views.artistregister,name='artistregister'),
    path('registerartist',views.registerartist,name='registerartist'),
    path('artist.html',views.artist,name='artist'),
    path('artist_single.html/<int:id>',views.artist_single,name='artist_single'),
    path('newplaylist.html',views.newplaylist,name='newplaylist'),
    path('playlist',views.playlist,name='playlist'),
]