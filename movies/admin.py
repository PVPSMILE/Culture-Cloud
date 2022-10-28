from unicodedata import category
from django import forms
from django.contrib import admin
# from django.contrib import mark_safe
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Rewiews
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="description", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)

class ShowRewiws(admin.TabularInline):#StackedInline, TabularInline
    model = Rewiews
    extra = 1#one empty fiel, dmore fields for rewiew
    readonly_fields = ("name", "email")

class ShowMovieShots(admin.StackedInline):
    movie = MovieShots
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display = ("id", "title", "category", "url", "draft")
    list_filter = ("category", "year")
    list_display_links = ("title",)
    search_fields = ("title", "category__name")
    inlines = [ShowRewiws, ]#ShowMovieShots
    save_on_top= True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    # fields = (("actors", "deirectors", "genres"),)
    fieldsets = (
        (None, {#1None can be a name of group 
            #2 u can also write for using function hide and show
            #"classes":("collapse",),
            "fields": ("title",)
        }),
        (None, {
            "fields": ("poster", "description",)
        }),
        (None, {
            "fields": (("country","world_premiere", "year"),)
        }),
        (None, {
            "fields": (("actors", "directors"), ("category", "genres"),)
        }),
        (None, { 
            "fields": (("budget", "fees_in_world"),)
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

@admin.register(Rewiews)
class RewiewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name","email", "parent", "movie")
    readonly_fields = ("name", "email")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    list_display = ("name", "age", "image")
    search_fields = ("name")
    search_fields = ("name", )
    

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
admin.site.register(MovieShots)


admin.site.site_title = "Culture Cloud"
admin.site.site_header = "Culture Cloud"