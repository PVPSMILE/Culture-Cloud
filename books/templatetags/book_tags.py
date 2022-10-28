from django import template
from books.models import Book, Genre


register = template.Library()

@register.simple_tag()
def get_categories():
    return Genre.objects.all()


@register.inclusion_tag('books/tags/last_update.html')
def get_last_updates():
    books = Book.objects.order_by("id")[:5]
    return {"last_updates": books}