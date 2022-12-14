from django.forms import ModelForm, PasswordInput, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'email': "Email",
            'password1': "Password",
            'password2': "Confirm password",
        }


class LoginUser(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password'
        }
        widgets = {
            "username":  TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}),
            "password": PasswordInput(attrs={'placeholder': '********', 'autocomplete': 'off'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        widgets = {
            "bio":  Textarea(attrs={'placeholder': 'Bio'}),
        }
