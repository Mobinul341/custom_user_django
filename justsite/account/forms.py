from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from . models import CustomUser

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required valid mail")

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'full_name', 'password1', 'password2']



class CustomAuthentication(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Email or Password")


        