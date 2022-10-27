from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm

def homeProject(request):
    return render(request, 'home.html')

def newProject(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/projects')
        
    else :
        form = ProjectForm()
        return render(request, 'projects/newProject.html', {'form': form})

           