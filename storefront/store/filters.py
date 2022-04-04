from django_filters import rest_framework as filters

from store.models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='unit_price', lookup_expr='gt')
    max_price = filters.NumberFilter(field_name='unit_price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['collection_id', 'min_price', 'max_price']
