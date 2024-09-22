from django import forms
from .models import Camiseta, Botin, Short

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        exclude = ['usuario']  # Excluir el campo usuario

class BotinForm(forms.ModelForm):
    class Meta:
        model = Botin
        exclude = ['usuario']  # Excluir el campo usuario

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Short
        exclude = ['usuario']  # Excluir el campo usuario
