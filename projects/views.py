from django.views.generic import UpdateView
from projects.models import Projeto
from django.shortcuts import render, redirect, get_object_or_404
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

def project_list(request):
    projects = Projeto.objects.all()
    return render(request, 'projects/list_all_projects.html', {'projects' : projects})

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = '__all__'

    def get_success_url(self):
        return '/'


update_view = ProjetoUpdateView.as_view()


def view_delete_project(request, pk):
    project = Projeto.objects.get(id=pk)
    project.delete()

    return redirect('/projetos/listar')


