from django.urls import path
from projects.views import new_project, home_project, update_project, project_list, delete_project

app_name = 'projects'

urlpatterns = [

    path('', home_project),
    path('registrar/', new_project, name='registrar'),
    path('listar/', project_list, name='listar'),
    path('listar/<int:pk>/editar', update_project, name='atualizar'),
    path('listar/<int:pk>/excluir', delete_project, name='excluir')

]
