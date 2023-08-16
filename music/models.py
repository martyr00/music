import os

from django.db import models
from django.contrib.auth.models import User


def album_upload_path(instance, filename):
    author = instance.author.username
    title_album = instance.album

    upload_path = os.path.join('', str(author), str(title_album), filename)
    return f"music/{upload_path}"


def music_upload_path(instance, filename):
    title_music = instance.title
    title_album_music = instance.album.title
    user = instance.author.username

    upload_path = os.path.join('', str(user), str(title_album_music), str(title_music), filename)
    return f"music/{upload_path}"


class Genre(models.Model):
    title = models.CharField(max_length=100, unique=True)


class Album(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to=album_upload_path)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums_authored')
    on_feat = models.ManyToManyField(User, related_name='albums_featured')
    genre = models.ManyToManyField(Genre, related_name='album_genre')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time')


class Music(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=music_upload_path)
    image = models.ImageField(upload_to=music_upload_path)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music_authored')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_music')

    on_feat = models.ManyToManyField(User, related_name='music_featured')
    in_fav = models.ManyToManyField(User, related_name='music_favorites')
    genre = models.ManyToManyField(Genre, related_name='genre')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time')


class PlayList(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='play_list_authored')
    music = models.ManyToManyField(Music, related_name='music_play_list')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time')
