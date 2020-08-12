from django import forms

# from django.utils.text import slugify
from links.models import Link


class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title', 'url', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'url'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'image': forms.FileInput()
        }
