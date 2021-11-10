from django_filters import rest_framework as filters
from .models import Order


class OrdersFilter(filters.FilterSet):
    created = filters.RangeFilter()

    class Meta:
        model = Order
        fields = ['created']
