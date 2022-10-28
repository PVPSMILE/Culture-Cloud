from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import Contact, Content
# from .forms import ContactForm
# from .servise import send
from books.models import Book
from movies.models import Movie, Actor


# class ContactView(CreateView):

#     model = Contact
#     form_class = ContactForm
#     success_url = "/"


def index(request):
   
    return render(request, 'public/index.html')

