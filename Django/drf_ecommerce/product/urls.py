from django.urls import path
from .views import CategoryViewSet, BrandViewSet, ProductViewSet

urlpatterns = [
    path("category/", CategoryViewSet.as_view({'get': 'list_category'})),
    path("brand/", BrandViewSet.as_view({"get":"list_brand"})),
    path("product/", ProductViewSet.as_view({"get":"list_product"}))
    ]