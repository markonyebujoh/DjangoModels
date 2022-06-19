from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default = "enter text here")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default = '')
    Published_date = models.DateTimeField(default = '')