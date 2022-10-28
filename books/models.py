from audioop import reverse
from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from datetime import date
# Create your models here.
class Genre(models.Model):

    name = models.CharField("Name",max_length=100)
    description = models.TextField("About")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

  
class Book(models.Model):

    name = models.CharField("Name", max_length=100)
    author = models.CharField("Author", max_length=100, default="Alice")
    short_description = models.TextField("Short Description")
    description = models.TextField("Full Description")
    poster = models.ImageField("Poster", upload_to="books/")
    year = models.PositiveSmallIntegerField("Realize", default=2019)
    genres = models.ManyToManyField(Genre, verbose_name = "genre")



    url = models.SlugField(max_length=160, unique=True) # unique - Уникальное поле
    draft = models.BooleanField("Draft", default=False)


    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta():
        verbose_name = "Book"
        verbose_name_plural = "Books"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)#значения от -32767 до 32767

    def __str__(self):
        return f'{self.value}'

    class Meta():
        verbose_name = "Value of rating"
        verbose_name_plural = "Values of rating"
        ordering = ["-value"]

class Rating(models.Model):

    ip = models.CharField("IP adress", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="film")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Raiting"
        verbose_name_plural = "Raitings"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Book, verbose_name="book", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
