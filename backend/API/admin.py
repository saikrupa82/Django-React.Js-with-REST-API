from django.contrib import admin
from django.contrib import admin
from .models import API

class APIAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(API, APIAdmin)