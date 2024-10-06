from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Product, User, Category
from .serializers import ProductSerializer, UserSerializer, CategorySerializer

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        category = self.request.GET.get('category')
        price_range = self.request.GET.get('price_range')
        stock_availability = self.request.GET.get('stock_availability')

        queryset = Product.objects.all()

        if category:
            queryset = queryset.filter(category__name=category)

        if price_range:
            min_price, max_price = price_range.split(',')
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        if stock_availability:
            queryset = queryset.filter(stock_quantity__gt=0)

        return queryset

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductSearchAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        name = request.GET.get('name')
        category = request.GET.get('category')

        queryset = Product.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)

        if category:
            queryset = queryset.filter(category__name=category)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
