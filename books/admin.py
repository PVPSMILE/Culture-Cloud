from unicodedata import category
# from django import forms
from django.contrib import admin
# from django.contrib import mark_safe
from .models import Book, Genre, Rating, RatingStar, Reviews
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class ShowRewiws(admin.TabularInline):#StackedInline, TabularInline
    model = Reviews
    extra = 1#one empty fiel, dmore fields for rewiew
    readonly_fields = ("name", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name", "url", "draft")
    
    list_display_links = ("name",)

    inlines = [ShowRewiws, ]#ShowMovieShots
    save_on_top= True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    # form = MovieAdminForm
    # fields = (("actors", "deirectors", "genres"),)
    fieldsets = (
        (None, {#1None can be a name of group 
            #2 u can also write for using function hide and show
            #"classes":("collapse",),
            "fields": ("name",)
        }),
        (None, {
            "fields": ("poster", "description", "short_description")
        }),
        (None, {
            "fields": ("year", "genres", )
        }),
        (None, {
            "fields": ("url", "draft",)
        }),
    )
    def unpublish(self, request, quaryset):

        row_update = quaryset.update(draft=True)
        if row_update == '1':
            message_bit = "1 update"
        else:
            message_bit = f"{row_update} updates"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, quaryset):

        row_update = quaryset.update(draft=False)
        if row_update == '1':
            message_bit = "1 update"
        else:
            message_bit = f"{row_update} updates"
        self.message_user(request, f"{message_bit}")

    publish.short_desription = "Publish"
    publish.allowed_permission = ('change', )

    unpublish.short_desription = "Unpublish"
    unpublish.allowed_permission = ('change', )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name","email", "parent")
    readonly_fields = ("name", "email")



    # def get_image(self, obj):
    #     return (f'<img scr={obj.poster.url} width="50" height="60')
    # get_image.short_description = "Imag32132e"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")



admin.site.register(RatingStar)


