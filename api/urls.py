from django.urls import path
from api import views

urlpatterns = [
    path('categorias/', views.category_list.as_view()),
    path('categorias/<int:pk>/', views.category_detail.as_view()),
    path('transacciones/', views.transaction_list.as_view()),
    path('transacciones/<int:pk>/', views.transaction_detail.as_view()),
]
