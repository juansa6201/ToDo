from .models import *
from django import forms


class FormToDo(forms.ModelForm):
    class Meta:
        model=ToDo
        fields=('message',)
        widgets = {
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el mensaje'
            })
        }