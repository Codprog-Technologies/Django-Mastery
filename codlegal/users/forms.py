from django import forms
from django.contrib.auth import authenticate


class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            self.user = user
        else:
            raise forms.ValidationError('Invalid Username or Password')

    def get_user(self):
        return self.user