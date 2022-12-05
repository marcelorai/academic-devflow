from django.shortcuts import render, redirect
from .forms import ArtefatoCreateForm
from artifacts.models import Artefato


def create_artifact_view(request):
    form = ArtefatoCreateForm()
    if request.method == 'POST':
        form = ArtefatoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:listar')
    return render(request, 'artifacts/novo-artefato.html', {'form': form})

def artifact_list(request):
    artifacts = Artefato.objects.all()
    return render(request, 'artifacts/list_all_artifacts.html', {'artifacts': artifacts})

def filter_artifact_by_name(request):
    name = request.GET.get('name')
    artifacts = Artefato.objects.filter(nome=name)
    return render(request, 'artifacts/home_artifacts.html', {'artifacts': artifacts})