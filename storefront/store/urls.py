from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pid>/', views.product_detail, name='product_detail'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:cid>/', views.collection_detail, name='collection-detail'),
]
