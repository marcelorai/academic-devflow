from django.shortcuts import render, redirect
from .forms import ArtefatoCreateForm
from artifacts.models import Artefato


def create_artifact_view(request):
    form = ArtefatoCreateForm()
    if request.method == 'POST':
        form = ArtefatoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artifacts:listar')
    return render(request, 'artifacts/novo-artefato.html', {'form': form})

def artifact_list(request):
    artifacts = Artefato.objects.all()
    return render(request, 'artifacts/list_all_artifacts.html', {'artifacts': artifacts})

def home_artifact(request):

    name = request.GET.get('nome', None)

    if name:
        artifacts = Artefato.objects.filter(nome__contains=name)
        return render(request, 'artifacts/home_artifacts.html', {'artifacts': artifacts})
    else:
        return render(request, 'artifacts/home_artifacts.html')