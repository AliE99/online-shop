from django.db.models import Count
from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.SerializerMethodField(method_name='count_products')

    def count_products(self, collection: Collection):
        return collection.product_set.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection', 'inventory']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax', read_only=True)

    # collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def create(self, validated_data):
    #     print(validated_data)
    #     return super().save()
