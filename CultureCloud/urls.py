from unicodedata import category
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from public.views import index




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    # path('tops/', tops, name='tops'), 
    # path('all/', categories, name='categories'),
    # path('tops/books/', books, name='books'),
    # path('book/<int:book_id>', post_info, name='book'),
    path('', include("movies.urls")), 
    path('', include("books.urls")),  
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('', include("public.urls")), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)