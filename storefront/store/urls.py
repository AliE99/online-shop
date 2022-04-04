from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CollectionViewSet
from pprint import pprint

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

urlpatterns = router.urls
