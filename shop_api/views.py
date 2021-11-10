from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, ScoreSerializer
from django.contrib.auth.models import User
from .models import Product, Order, Score
from .service import OrdersFilter


class UserList(generics.ListAPIView):
    '''User List, we can see all our users in system.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    '''User detail, only admin has permission for look this list.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductListAPIView(generics.ListAPIView):
    '''Product List, we can see all added product for order.'''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetail(generics.ListAPIView):
    #Detailed information about product.
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderListAPIView(generics.ListAPIView):
    '''List all orders in database.'''
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrdersFilter
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderCreateAPIView(generics.ListCreateAPIView):
    '''Create new order from product.'''
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ScoreListAPIView(generics.ListAPIView):
    '''List all scores.'''
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ScoreDetail(generics.ListCreateAPIView):
    '''Create score from order'''
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    permission_classes = [permissions.IsAuthenticated]



