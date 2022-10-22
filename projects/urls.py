from django.urls import path

from projects.views import update_view

app_name = 'projects'

urlpatterns = [
    path('<int:pk>/editar', update_view, name='update'),
]