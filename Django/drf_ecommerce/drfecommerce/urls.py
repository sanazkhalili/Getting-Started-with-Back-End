
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view



#router = DefaultRouter()
#router.register(r'category', views.CategoryViewSet, basename="category")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls")),
  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
