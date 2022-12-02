from django.shortcuts import render, redirect
from .forms import ArtefatoCreateForm


def create_artifact_view(request):
    form = ArtefatoCreateForm()
    if request.method == 'POST':
        form = ArtefatoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'artifacts/novo-artefato.html', {'form': form})
