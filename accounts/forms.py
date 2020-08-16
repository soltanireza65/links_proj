from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input_user border-input', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input_pass', 'placeholder': 'Password'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control input_pass', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control input_pass', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control input_user border-input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input_email', 'placeholder': 'Email'})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'display_name', 'bio', 'instagram_url', 'youtube_url', 'twitter_url', 'facebook_url')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control input_user  avatar_input form_input'}),
            'display_name': forms.TextInput(
                attrs={'class': 'form-control  form_input border-input', 'placeholder': 'Display Name'}),
            'bio': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Bio'}),
            'instagram_url': forms.TextInput(
                attrs={'class': 'form-control border-input form_input', 'placeholder': 'Instagram Url'}),
            'youtube_url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Youtube Url'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Twitter Url'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control border-input form_input', 'placeholder': 'Facebook Url'})
        }
