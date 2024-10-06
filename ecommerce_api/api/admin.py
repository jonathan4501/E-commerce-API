from django.contrib import admin
from .models import Product, Category, User

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)

