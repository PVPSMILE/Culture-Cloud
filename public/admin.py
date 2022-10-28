from django.contrib import admin
from .models import Contact, Content
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "date")

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name",)
    