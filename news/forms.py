from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
        ]


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
        ]
