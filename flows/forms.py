from django import forms
from .models import Fluxo


class CriarFluxoForm(forms.ModelForm):
    class Meta:
        model = Fluxo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
