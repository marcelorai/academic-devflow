from django.urls import path
from artifacts.views import create_artifact_view

app_name = 'artifacts'

urlpatterns = [
    path('registrar/', create_artifact_view, name='registrar'),
]
