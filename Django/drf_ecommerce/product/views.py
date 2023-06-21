from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Brand, Product
from .serializer import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.response import Response



class CategoryViewSet(viewsets.ViewSet):
    """
     show all category
    """
    query = Category.objects.all()
    def list_category(self, request):
        seri_category = CategorySerializer(self.query, many=True)
        return Response(seri_category.data)


class BrandViewSet(viewsets.ViewSet):
    """
     show all brands
    """
    query = Brand.objects.all()
    def list_brand(self, request):
        seri_brand =BrandSerializer(self.query, many=True)
        return Response(seri_brand.data)
    

class ProductViewSet(viewsets.ViewSet):
    """
     show all products
    """
    query = Product.objects.all()
    def list_product(self, request):
        seri_pro =ProductSerializer(self.query, many=True)
        return Response(seri_pro.data)

