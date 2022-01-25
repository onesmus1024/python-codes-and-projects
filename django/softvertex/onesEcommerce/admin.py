from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields=['name','description','image','category']