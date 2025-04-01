from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'