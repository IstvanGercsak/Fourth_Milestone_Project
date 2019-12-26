from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, default="")
    description_section_1 = models.TextField(default="")
    description_section_2 = models.TextField(default="")
    description_section_3 = models.TextField(default="")
    slug = models.SlugField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description_section_1[:450] + "....."


class Comment(models.Model):

    post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
