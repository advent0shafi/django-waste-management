from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category_id')

    class Meta:
        model = Product
        fields = ['category']
