from django.shortcuts import render, redirect, get_object_or_404
from .models import Fluxo
from .forms import CriarFluxoForm


def pagina_inicial_view(request):
    fluxos = Fluxo.objects.all()
    return render(request, 'flows/fluxo/home.html', {'fluxos': fluxos})


def adicionar_fluxo_view(request):
    form = CriarFluxoForm()
    if request.method == 'POST':
        form = CriarFluxoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flows:inicio')
    return render(request, 'flows/fluxo/adicionar.html', {'form': form})


def detalhes_fluxo_view(request, pk):
    fluxo = get_object_or_404(Fluxo, id=pk)
    return render(request, 'flows/fluxo/detalhes.html', {'fluxo': fluxo})
