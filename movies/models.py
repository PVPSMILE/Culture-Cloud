from audioop import reverse
from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from datetime import date

# Create your models here.
class Category(models.Model):

    name = models.CharField("Category", max_length=150)
    description = models.TextField("About")
    url = models.SlugField(max_length=160, unique=True) # unique - Уникальное поле

    #строковое предстваление нашей модели
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    


    

class Genre(models.Model):

    name = models.CharField("Name",max_length=100)
    description = models.TextField("About")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

class Actor(models.Model):
    
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0) #PositiveBigIntegerField допускает положительные значения от 0-32767
    born = models.DateField("Born", default=date.today)
    start_acting = models.PositiveSmallIntegerField("Start", default=1980)
    end_acting = models.CharField("End", max_length=100, default="present")
    genre = models.CharField("Name", max_length=100, default="Adventure, Drama")
    nationality = models.CharField("Nationality", max_length=100,  default="USA")
    description = models.TextField("About")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor', kwargs={"slug": self.name})
        
    class Meta:
        verbose_name = "Actor and director"
        verbose_name_plural = "Actors and directors"
  
class Movie(models.Model):

    title = models.CharField("Title", max_length=100)
    description = models.TextField("About")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Realize", default=2019)
    country = models.CharField("Country", max_length=100)
    directors = models.ManyToManyField(Actor,  verbose_name = "director", related_name="film_director")
    actors = models.ManyToManyField(Actor,  verbose_name = "actor", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name = "genre")
    world_premiere = models.DateField("Date of Premiere in the world", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="only in dollars")

    fees_in_world = models.PositiveIntegerField(
        "Fees in World", default=0, help_text="only in dollars"
    )
    category = models.ForeignKey(
        Category, verbose_name="Cateory", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True) # unique - Уникальное поле
    draft = models.BooleanField("Draft", default=False)


    def get_review(self):
        return self.rewiews_set.filter(parent__isnull=True)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta():
        verbose_name = "Film"
        verbose_name_plural = "Films"
    

    
class MovieShots(models.Model):

    title = models.CharField("Title",max_length=100)
    description = models.TextField("About")
    image = models.ImageField("Image", upload_to = "movie_shouts/")
    movie = models.ForeignKey(Movie, verbose_name="Film", on_delete=models.CASCADE)#при удалении фильма так же удаляться и кадры

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Short part of film"
        verbose_name_plural = "Short parts of film"

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="film")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Raiting"
        verbose_name_plural = "Raitings"

class Rewiews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="film", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
