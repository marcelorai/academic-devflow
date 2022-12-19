from django.shortcuts import get_object_or_404, redirect, render

from .forms import AtualizarEtapaForm, CriarEtapaForm, CriarFluxoForm
from .models import Etapa, Fluxo


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


def adicionar_etapa_view(request, fluxo_pk):
    fluxo = get_object_or_404(Fluxo, id=fluxo_pk)
    form = CriarEtapaForm()
    if request.method == 'POST':
        form = CriarEtapaForm(request.POST)
        if form.is_valid():
            etapa = form.save(commit=False)
            etapa.fluxo = fluxo
            etapa.save()
            return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/adicionar.html', {'form': form, 'fluxo': fluxo})


def editar_etapa_view(request, fluxo_pk, pk):
    etapa = get_object_or_404(Etapa, id=pk)
    fluxo = get_object_or_404(Fluxo, id=fluxo_pk)
    form = AtualizarEtapaForm(instance=etapa)
    if request.method == 'POST':
        form = AtualizarEtapaForm(request.POST)
        if form.is_valid():
            nova_etapa = form.save(commit=False)
            nova_etapa.fluxo = fluxo
            nova_etapa.id = pk
            nova_etapa.save()
            return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/editar.html', {'form': form, 'etapa': etapa})


def excluir_etapa_view(request, fluxo_pk, pk):
    etapa = get_object_or_404(Etapa, id=pk)
    if request.method == 'POST':
        etapa.delete()
        return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/excluir.html', {'etapa': etapa})
