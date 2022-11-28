from django.urls import path
from projects.views import newProject, homeProject, update_view, project_list, view_delete_project

app_name = 'projects'

urlpatterns = [

    path('', homeProject),
    path('registrar/', newProject, name='registrar'),
    path('listar/', project_list, name='listar'),
    path('<int:pk>/editar', update_view, name='update'),
    path('listar/<int:pk>/excluir', view_delete_project, name='excluir')

]
