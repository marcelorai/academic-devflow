from django import forms

from .models import Artefato



class ArtefatoCreateForm(forms.ModelForm):
    class Meta:
        model = Artefato
        fields = ['nome', 'descricao', 'situacao', 'data_entrega']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'situacao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'type':'date', 'class': 'form-control'})
        }
