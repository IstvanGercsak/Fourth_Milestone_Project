from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, default="")
    description = models.TextField()
    slug = models.SlugField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # We show the first 50 characters
    def snippet(self):
        return self.description[:450] + "....."
