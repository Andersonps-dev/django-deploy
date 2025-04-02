from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(name='index')),   
    path('deletar_produto/<int:pk>/', ProdutoDeleteView.as_view(name='deletar_produto')),   
]