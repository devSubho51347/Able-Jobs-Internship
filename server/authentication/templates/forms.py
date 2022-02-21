from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class createUserForm(UserCreationForm):

    password1 = forms.PasswordInput()
    ## Retype your password
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1','password2']
        widgets = {
            'first_name': forms.TextInput(),
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
        }