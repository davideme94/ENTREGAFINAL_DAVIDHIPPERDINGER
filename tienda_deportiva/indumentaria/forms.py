from django import forms
from .models import Camiseta, Botin, Short

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        fields = '__all__'

class BotinForm(forms.ModelForm):
    class Meta:
        model = Botin
        fields = '__all__'

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = '__all__'
