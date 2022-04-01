from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pid>/', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:cid>/', views.collection_detail, name='collection-detail'),
]
