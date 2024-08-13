from api.models import Category, Transaction
from api.serializers import CategorySerializer, TransactionSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class category_list(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    '''def get(self, request, format=None):
        categorias = Category.objects.all()
        serializer = CategorySerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
    
class transaction_list(generics.ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    '''
    def get(self, request, format=None):
        transacciones = Transaction.objects.all()
        serializer = TransactionSerializer(transacciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
    
class category_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    '''
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
                
    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategorySerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategorySerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    '''
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404
                
    def get(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransactionSerializer(transaccion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransactionSerializer(transaccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        transaccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
