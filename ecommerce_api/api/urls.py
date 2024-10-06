from django.urls import include, path
from rest_framework import routers
from .views import (
    ProductListAPIView,
    ProductRetrieveAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    ProductSearchAPIView,
)


urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('products/create/', ProductCreateAPIView.as_view()),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('products/<int:pk>/delete/', ProductDestroyAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('users/create/', UserCreateAPIView.as_view()),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view()),
    path('users/<int:pk>/delete/', UserDestroyAPIView.as_view()),
    path('products/search/', ProductSearchAPIView.as_view()),
]