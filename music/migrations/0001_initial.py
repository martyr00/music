# Generated by Django 4.2.3 on 2023-08-16 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=music.models.album_upload_path)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums_authored', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=music.models.music_upload_path)),
                ('image', models.ImageField(upload_to=music.models.music_upload_path)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_music', to='music.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_authored', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ManyToManyField(related_name='genre', to='music.genre')),
                ('in_fav', models.ManyToManyField(related_name='music_favorites', to=settings.AUTH_USER_MODEL)),
                ('on_feat', models.ManyToManyField(related_name='music_featured', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_list_authored', to=settings.AUTH_USER_MODEL)),
                ('music', models.ManyToManyField(related_name='music_play_list', to='music.music')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(related_name='album_genre', to='music.genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='on_feat',
            field=models.ManyToManyField(related_name='albums_featured', to=settings.AUTH_USER_MODEL),
        ),
    ]
