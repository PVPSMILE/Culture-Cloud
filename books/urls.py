from django.urls import path 
from . import views

urlpatterns = [
    path('books/', views.BooksView.as_view(), name = 'books'),
    path('book_filter/', views.FilterBooksView.as_view(), name = 'book_filter'),
    path('book_search/', views.Search.as_view(), name = 'book_search'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name="book_detail"),
    path('book_review/<int:pk>/', views.BookAddReview.as_view(), name="book_add_review"),
]