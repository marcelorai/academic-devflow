from django import forms

from .models import Etapa, Fluxo
from django.core.exceptions import ValidationError


class CriarFluxoForm(forms.ModelForm):
    class Meta:
        model = Fluxo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CriarEtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['nome', 'numero', 'descricao', 'data_inicio',
                  'data_finalizacao', 'gameficada']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_finalizacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gameficada': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'})
        }

        labels = {
            'gameficada': 'Usar gameficação'
        }

        help_texts = {
            'numero': 'Posição da etapa dentro do fluxo'
        }

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_finalizacao = cleaned_data.get('data_finalizacao')

        if data_inicio and data_finalizacao:
            if data_inicio > data_finalizacao:
                mensagem = "A etapa não pode iniciar após sua data de finalização"
                self.add_error('data_inicio', mensagem)


class AtualizarEtapaForm(CriarEtapaForm):
    def __init__(self, *args, **kwargs):
        super(AtualizarEtapaForm, self).__init__(*args, **kwargs)
        if self.instance.data_inicio:
            self.initial['data_inicio'] = self.instance.data_inicio.isoformat()
        if self.instance.data_finalizacao:
            self.initial['data_finalizacao'] = self.instance.data_finalizacao.isoformat()
