from api.models import Category, Transaction
from api.serializers import CategorySerializer, TransactionSerializer
from rest_framework import generics


class category_list(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class transaction_list(generics.ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class category_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
