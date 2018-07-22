from django import forms
from .models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ('degree', 'major',)

class UserCompletedForm(forms.ModelForm):
    class Meta:
        model = Complete
        fields = ('user', 'complete')