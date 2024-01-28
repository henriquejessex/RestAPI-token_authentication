from django import forms
from register.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email', 'address', 'phone', 'password']
        widget = {'password': forms.PasswordInput()}
