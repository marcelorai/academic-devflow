from pyexpat import model
from django import forms 

from .models import Projeto

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ('descricao', 'dt_inicio', 'dt_termino', 'nome', 'situacao')
        