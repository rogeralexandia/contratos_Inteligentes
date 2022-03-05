from django.urls import path
from core.api.views import *

urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category_delete'),
    path('product/list/', ProductListAPIView.as_view(), name='product_list'),
]
