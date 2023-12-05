from django.contrib import admin

from storeapp.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','qty','cat','is_active']
    list_filter=['price']

admin.site.register(Product,ProductAdmin)
