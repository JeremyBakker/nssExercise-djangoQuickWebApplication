from django.db import models


class Artist(models.Model):
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.artist


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title
