from django.urls import path
from projects.views import update_view, project_list

app_name = 'projects'

urlpatterns = [
    path('project_list/', project_list, name='project_list'),
    path('<int:pk>/editar', update_view, name='update'),
    # path('project_detail/<int:pk>', project_detail, name='project_detail' ),
]
