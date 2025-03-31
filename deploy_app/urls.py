from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
]