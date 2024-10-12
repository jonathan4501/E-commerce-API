from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Product, User, Category
from rest_framework.exceptions import PermissionDenied
from .serializers import ProductSerializer, UserSerializer, CategorySerializer
import django_filters
from rest_framework.renderers import BrowsableAPIRenderer
class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]

    def perform_destroy(self, instance):
        if self.request.user == instance.owner or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this product.")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff or request.user == instance.owner:
            return super().update(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to update this product.")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff or request.user == instance.owner:
            return super().retrieve(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to view this product's details.")

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProductPagination

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]

    def perform_destroy(self, instance):
        if self.request.user == instance or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this user.")

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.id == kwargs.get('pk'):
            return super().update(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to update this user.")

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.id == kwargs.get('pk'):
            return super().retrieve(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to view this user's details.")
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
