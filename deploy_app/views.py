from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        context['form'] = ProdutoForm()
        return context

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('index')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
    
       