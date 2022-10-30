from django.urls import path

from projects.views import newProject, homeProject

app_name = 'projects'

urlpatterns = [
    path('', homeProject),
    path('registrar/', newProject, name='register')
]
