from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genre"

    def __str__(self):
            return self.name
        
class Content(models.Model):
    MOVIE = 'movie'
    TV_SHOW = 'tv_show'
    SERIES = 'series'
    TYPE_CHOICES = [
        (MOVIE, 'Movie'),
        (TV_SHOW, 'TV Show'),
        (SERIES, 'Series'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    genres = models.ManyToManyField("Genre", blank=True, related_name="contents")

    class Meta:
        db_table = "content"

    def __str__(self):
        return f"{self.title} ({self.type})"

class Episode(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    season_number = models.IntegerField()
    episode_number = models.IntegerField()

    class Meta:
        db_table = "episode"

    def __str__(self):
        return f"{self.content.title} – Episode {self.episode_number}: {self.title}"

