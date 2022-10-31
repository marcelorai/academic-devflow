from django.urls import path

from projects.views import update_view, get_All_Projects,project_detail

app_name = 'projects'

urlpatterns = [
    path('', get_All_Projects, name='get'),
    path('<int:pk>/editar', update_view, name='update'),
    path('project-detail/<int:pk>', project_detail, 'view' )
]
