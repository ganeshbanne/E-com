from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ecom.serializers import ProductSerializer
from ecom.models import Product

class ProductOperations(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
