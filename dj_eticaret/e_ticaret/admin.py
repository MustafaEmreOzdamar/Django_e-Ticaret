from django.contrib import admin
from .models import Product


# Register your models here.
# e_ticaret/admin.py

"""@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name', 'description')"""

admin.site.register(Product)
