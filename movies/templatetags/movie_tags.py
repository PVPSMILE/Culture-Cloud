from django import template
from movies.models import Category, Movie


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('movies/tags/last_update.html')
def get_last_updates():
    movies = Movie.objects.order_by("id")[:3]
    return {"last_updates": movies}