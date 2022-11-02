from django import forms 
from .models import Projeto

class ProjectForm(forms.ModelForm):
    
    
    class Meta:
        model = Projeto
        fields = '__all__'
        options = (
        ('Default', 'Selecione'),
        ('Iniciado','Iniciado'),
        ('Interrompido','Interrompido'),
        ('Finalizado','Finalizado') )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form__field'}),
            'descricao': forms.Textarea(attrs={'class': 'form__field'}),
            'data_inicio': forms.TextInput(attrs={'class': 'form__field', 'type': 'date'}),
            'data_termino': forms.TextInput(attrs={'class': 'form__field', 'type': 'date'}),
            'situacao': forms.Select(choices = options)
        }
        