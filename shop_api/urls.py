from django.urls import path, include
from .views import ProductListAPIView, ProductDetail, OrderCreateAPIView,\
    OrderListAPIView, ScoreListAPIView, ScoreDetail


urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('orders/', OrderListAPIView.as_view()),
    path('orders/<int:pk>/', OrderCreateAPIView.as_view()),
    path('scores/', ScoreListAPIView.as_view()),
    path('scores/<int:pk>/', ScoreDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

