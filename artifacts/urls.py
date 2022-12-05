from django.urls import path
from artifacts.views import create_artifact_view, update_artifact, delete_artifact

app_name = 'artifacts'

urlpatterns = [
    path('registrar/', create_artifact_view, name='registrar'),
    path('listar/<int:pk>/editar', update_artifact, name='update_artifact'),
    path('listar/<int:pk>/excluir', delete_artifact, name='delete_artifact')
]
