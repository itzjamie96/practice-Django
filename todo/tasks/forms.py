from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):

    # input text
    singleTask = forms.CharField(max_length=100)

    # need to give minimal of two values
    class Meta:
        # which model do you want to create a form for?
        model = Task

        # what fields are we gonna allow?
        fields = '__all__'