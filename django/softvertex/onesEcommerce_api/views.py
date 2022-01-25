import imp
from django.shortcuts import render
from rest_framework import generics

from onesEcommerce.models import Products
from onesEcommerce_api.serializers import ProductSerializer

class ProductViewApi(generics.ListAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
