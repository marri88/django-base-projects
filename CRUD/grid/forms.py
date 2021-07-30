from django import forms
from .models import Employer


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }
