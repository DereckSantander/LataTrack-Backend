from api.models import Category, Transaction, Report
from api.serializers import CategorySerializer, TransactionSerializer, ReportSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TransactionFilter, CategoryFilter


class category_list(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    
class transaction_list(generics.ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    
class category_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class report_list(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
class report_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer