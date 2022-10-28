from datetime import date
import email
from django.db import models

class Contact(models.Model):

    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Content(models.Model):

    name = models.CharField("Name", max_length=100)
    poster = models.ImageField("Poster", upload_to="main/")
    url = models.SlugField(max_length=160, unique=True, default="films")

    def __str__(self):
        return self.name