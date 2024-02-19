from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from sustainability.models import PlantOfTheDay


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PlantOfTheDayForm(forms.ModelForm):
    class Meta:
        model = PlantOfTheDay
        fields = ['plant']
