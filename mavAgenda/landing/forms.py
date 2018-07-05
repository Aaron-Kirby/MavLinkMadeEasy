from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)