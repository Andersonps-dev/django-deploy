from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    form = ProdutoForm()

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')

    return render(request, 'lista.html', {'produtos': produtos, 'form': form})