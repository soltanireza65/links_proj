from django import forms

# from django.utils.text import slugify
from links.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title', 'url', 'description', 'image', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Title'}),
            'url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'URL'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control border-input form_input', 'placeholder': 'Description'}),
            'image': forms.FileInput(
                attrs={'class': 'form-control border-input form_input file_input', 'id': 'file_input'})
        }

# class LinkCreateForm(forms.ModelForm):
#     class Meta:
#         model = Link
#         fields = ('title', 'url', 'description', 'image',)
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Title'}),
#             'url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'URL'}),
#             'description': forms.Textarea(
#                 attrs={'class': 'form-control border-input form_input', 'placeholder': 'Description'}),
#             'image': forms.FileInput(
#                 attrs={'class': 'form-control border-input form_input file_input', 'id': 'file_input'})
#         }
#
#
# class LinkUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Link
#         fields = ('title', 'url', 'description', 'image', 'is_active')
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Title'}),
#             'url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'URL'}),
#             'description': forms.Textarea(
#                 attrs={'class': 'form-control border-input form_input', 'placeholder': 'Description'}),
#             'image': forms.FileInput(
#                 attrs={'class': 'form-control border-input form_input file_input', 'id': 'file_input'})
#         }
