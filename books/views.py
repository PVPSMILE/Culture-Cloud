from multiprocessing import context
from turtle import title
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from audioop import reverse
from pickle import FALSE
from re import template
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Book, Genre, Rating, Reviews
from .forms import BookReviewForm, RatingForm


class GenreYears:
    
    def get_genres(self):
        return Genre.objects.all()

class BooksView(ListView, GenreYears):
        
    model = Book
    quaryset = Book.objects.all()
    
  
class BookDetailView(DetailView, GenreYears):    
    model = Book
    slug_field = "url"

class BookAddReview(View):
    def post(self, request, pk):
        form = BookReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book = book
            form.save()

        return redirect("/")

class FilterBooksView(ListView, GenreYears):
    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset



class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                book_id=int(request.POST.get("book")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)



class Search(ListView, GenreYears):

    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get("q"))
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
      