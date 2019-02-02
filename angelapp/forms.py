from django import forms

from .models import quotes

class PostForm(forms.ModelForm):

    class Meta:
        model = quotes
        exclude = ('firebase_id',)