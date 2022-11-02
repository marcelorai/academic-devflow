from django.views.generic import UpdateView
from projects.models import Projeto
from django.shortcuts import render, redirect
from .forms import ProjectForm

def homeProject(request):
    return render(request, 'projects/home.html')

def newProject(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/projetos')
        
    else :
        form = ProjectForm()
        return render(request, 'projects/newProject.html', {'form': form})

          
class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = '__all__'

    def get_success_url(self):
        return '/'


update_view = ProjetoUpdateView.as_view()

def project_list(request):
    lista_projetos = Projeto.objects.all()
    return render(request, 'projects/index.html', {'projects' : lista_projetos})
