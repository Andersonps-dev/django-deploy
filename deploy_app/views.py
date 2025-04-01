from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import View

class IndexView(View):
    
    def get(self, request):
        produtos = Produto.objects.all()
        form = ProdutoForm()
        return render(request, 'lista.html', {'produtos': produtos, 'form': form})
    
    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
        produtos = Produto.objects.all()
        return render(request, 'lista.html', {'produtos': produtos, 'form': form})