from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from ecom.serializers import ProductSerializer
from ecom.models import Product

class ProductOperations(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ["create","update","partial_update","destroy"]:
            self.permission_classes =(IsAuthenticated,)
        return super().get_permissions()