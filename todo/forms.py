from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError  

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title"]
        widgets = {
            'title': TextInput(attrs={
                'placeholder':'Inserisci una task...',
                'class':'add-task-text',
                'label':' '
            }) 
        }

class RegisterUser(UserCreationForm):
    username = forms.CharField(required=True, min_length=6, max_length=30)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
