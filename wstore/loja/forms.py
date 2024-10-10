from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'}),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        help_text="", 
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}),
        help_text="",  
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
