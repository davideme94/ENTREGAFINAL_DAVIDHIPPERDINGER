from django import forms
from .models import Camiseta, Botin, Short

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        exclude = ['usuario']  

class BotinForm(forms.ModelForm):
    class Meta:
        model = Botin
        exclude = ['usuario']  

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Short
        exclude = ['usuario']  
