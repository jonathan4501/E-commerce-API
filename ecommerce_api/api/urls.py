from django.urls import path
from .views import (
    ProductListView,
    UserCreateAPIView,
    ProductCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    UserRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/create', ProductCreateAPIView.as_view()),
    path('users/', UserCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    
]