from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import AuthorCreatedSerializer, ProductViewSets, CategoryViewSets


# routers
router = DefaultRouter()
router.register(r'Author', AuthorCreatedSerializer)
router.register(r'products', ProductViewSets)
router.register(r'categories', CategoryViewSets)


urlpatterns = [
    path('', include(router.urls))
]

