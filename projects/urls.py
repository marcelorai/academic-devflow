from django.urls import path

from projects.views import update_view, project_list,project_detail

app_name = 'projects'

urlpatterns = [
    path('project_list/', project_list, name='project_list'),
    path('<int:pk>/editar', update_view, name='update'),
    # path('project-detail/<int:pk>', project_detail, 'view' )
]
