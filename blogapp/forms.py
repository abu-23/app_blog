from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
        }
