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

           