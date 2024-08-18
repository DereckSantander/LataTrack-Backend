from rest_framework import serializers
from api.models import Category,Transaction, Report

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        #fields = ['id','name','type']
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        #fields = ['id', 'amount', 'description', 'category']
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'