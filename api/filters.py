from django_filters import rest_framework as filters
from .models import Transaction

class TransactionFilter(filters.FilterSet):
    category_type = filters.CharFilter(field_name='category__type')
    created_before = filters.DateFilter(field_name='created', lookup_expr='lte')
    created_after = filters.DateFilter(field_name='created', lookup_expr='gte')

    class Meta:
        model = Transaction
        fields = ['category_type','created_before', 'created_after']