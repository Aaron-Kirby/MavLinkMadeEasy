from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'degree')


class UserCompletedForm(forms.ModelForm):
    class Meta:
        model = Complete
        fields = ('user', 'complete')