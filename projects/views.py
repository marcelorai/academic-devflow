from django.views.generic import UpdateView
from django.shortcuts import render
from projects.models import Projeto


class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = '__all__'

    def get_success_url(self):
        return '/'


update_view = ProjetoUpdateView.as_view()

def get_All_Projects(request):
    lista_projetos = Projeto.objects.all()
    return render(request, 'projects/index.html', {'projects' : lista_projetos})