from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description', 'website', 'email']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
