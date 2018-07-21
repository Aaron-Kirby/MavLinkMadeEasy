from django import forms
from betterforms.multiform import MultiModelForm
from .models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ('degree', 'major',)

class UserForm(MultiModelForm):
    form_classes = {
        'email': EmailForm,
        'degree': DegreeForm,
    }

class UserCompletedForm(forms.ModelForm):
    class Meta:
        model = Complete
        fields = ('user', 'complete')