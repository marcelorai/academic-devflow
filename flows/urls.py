from django.urls import path
from .views import pagina_inicial_view

app_name = 'flows'

urlpatterns = [
    path('', pagina_inicial_view, name='inicio'),
]
