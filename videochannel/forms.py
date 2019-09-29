from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location=forms.CharField( required=True)

    class Meta:
        model = User

        fields = ('username', 'birth_date', 'password1', 'password2','location' )


class EditProfilePage(ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields=['bio', 'location','birth_date']