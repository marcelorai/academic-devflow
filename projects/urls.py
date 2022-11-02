from django.urls import path
from projects.views import newProject, homeProject, update_view, project_list

app_name = 'projects'

urlpatterns = [

    path('project_list/', project_list, name='project_list'),
    path('', homeProject),
    path('<int:pk>/editar', update_view, name='update'),
    path('registrar/', newProject, name='registrar')

]
