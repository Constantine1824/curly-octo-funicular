from django.contrib import admin
from .models import Recipes

list_display = ['title', 'author', 'ratings']
admin.site.register(Recipes, list_display=list_display)

# Register your models here.
