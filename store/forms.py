from django import forms
from django.contrib.auth.forms import UserCreationForm,User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        friends = ('username','email','password','password2')
