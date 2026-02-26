from django.contrib import admin
from .models import Service, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration', 'provider')
    list_filter = ('category', 'provider')
    search_fields = ('name', 'description')