from django.contrib import admin
from .models import Product, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'available', 'created',
                    'updated')
    list_display_links = ('id', 'name')
    list_filter = ('available', 'created')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}