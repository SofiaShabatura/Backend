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
    
