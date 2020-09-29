from django import forms
from django.forms import ModelForm
from .models import *

class PollForm(forms.ModelForm):

    question = forms.CharField(
        label = '제목',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'rows':5,
            'cols':100
        })
    ) 

    choice1 = forms.CharField(
        label='Choice 1',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'maxlength':100
        })
    )

    choice2 = forms.CharField(
        label='Choice 2',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'maxlength':100
        })
    )

    class Meta:
        model = Poll
        exclude = ['choice1_count', 'choice2_count']
