from django.shortcuts import render, HttpResponse


def create_artifact_view(request):
    return HttpResponse("<h1>Criar artefato</h1>")
