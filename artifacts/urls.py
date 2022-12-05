from django.urls import path
from artifacts.views import create_artifact_view, artifact_list, filter_artifact_by_name

app_name = 'artifacts'

urlpatterns = [
    path('', filter_artifact_by_name, name='home'),
    path('registrar/', create_artifact_view, name='registrar'),
    path('listar/', artifact_list, name='listar'),
]
