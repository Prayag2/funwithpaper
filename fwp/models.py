from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=200)
    image_link = models.CharField(max_length=500, null=True)
    pub_date = models.DateField(auto_now=True, null=True)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    user_views = models.IntegerField(default=0)
    tutorial_video_id = models.CharField(max_length=200, null=True, blank=True)
    template_link = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}    |    {self.pub_date}"

class Request(models.Model):
    your_name = models.CharField(max_length=200)
    suggestion = models.CharField(max_length=200)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.your_name} said '{self.suggestion}' on {self.date}"
