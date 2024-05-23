from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .models import Product, Brand, Category
from .permissions import IsOwnerOrAdminOrDirector


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['create',
                           'update',
                           'partial_update',
                           'retrieve',
                           'destroy']:
            return [IsOwnerOrAdminOrDirector()]
        return super().get_permissions()


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['create',
                           'update',
                           'partial_update',
                           'retrieve',
                           'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create',
                           'update',
                           'partial_update',
                           'retrieve',
                           'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()
