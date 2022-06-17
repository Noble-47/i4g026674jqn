from django.contrib.auth import get_user_model
from django.db import models

"""
 Post
 --------
Title : A string of maxlength 200, use Django’s models.CharField
Text : Any amount of text, use Django’s TextField
Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
Created_date : A date-time column, use Django’s models.DateTimeField.
Published_date : A date-time column, use Django’s models.DateTimeField.
"""
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField()
