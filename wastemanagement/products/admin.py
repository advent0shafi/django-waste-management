from django.contrib import admin
from .models import Category, Product, Color, Size, ProductImage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImage)

