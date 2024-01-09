from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms


class PerfilForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].requerid = True
        self.fields['last_name'].requerid = True
        self.fields['username'].requerid = True
        self.fields['email'].requerid = True
        self.fields['password'].requerid = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', ]
        labels = {'username': 'Username'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),


        }