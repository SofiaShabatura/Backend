from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    class Meta:
        db_table = "content"

    def __str__(self):
        return self.title


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