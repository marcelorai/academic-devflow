from django.shortcuts import render
from django.http import HttpResponse

def postProject(request):
    return render(request, 'projects/form_post_project.html')