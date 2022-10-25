from django.urls import path

from projects.views import postProject

app_name = 'projects'

urlpatterns = [
    path('register/', postProject)
]
