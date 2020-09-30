from django import forms
from django.forms import ModelForm
from .models import Article


class ArticleForm(forms.ModelForm):

    # ArticleForm에 대한 meta data
    class Meta:
        # which model do you want to create a form for?
        model = Article

        # what fields are we gonna allow?
        fields = '__all__'