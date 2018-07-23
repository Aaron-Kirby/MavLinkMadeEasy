from django import forms

'''
@LoginForm collection of fields corresponding to attributes
@forms.Form: associated data within fields
'''
class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)