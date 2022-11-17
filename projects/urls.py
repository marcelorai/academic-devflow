from django.urls import path
from projects.views import newProject, homeProject, update_view, project_list

app_name = 'projects'

urlpatterns = [

    path('', homeProject),
    path('listar/', project_list, name='project_list'),
    path('<int:pk>/editar', update_view, name='update'),
    path('registrar/', newProject, name='registrar')

]
