from django.urls import path
from projects.views import newProject, homeProject, update_view

app_name = 'projects'

urlpatterns = [

    path('', homeProject),
    path('<int:pk>/editar', update_view, name='update'),
    path('registrar/', newProject, name='registrar')

]
