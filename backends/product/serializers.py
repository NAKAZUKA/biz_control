from rest_framework import serializers

from .models import Product, Brand, Category


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id',
                  'title',
                  'brand',
                  'brand_name',
                  'category',
                  'category_name',
                  'price',
                  'quantity']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get_brand_name(self, obj):
        if obj.brand:
            return obj.brand.title
        else:
            return None

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.title
        else:
            return None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']
