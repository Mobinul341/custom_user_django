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
    #email = forms.EmailField(max_length=100, help_text="Required valid mail", widget=forms.TextInput)
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Email or Password")



class CustomUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email','username']

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('Email %s is already exists'%email)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('Username %s is already exists'%username)
        

            
