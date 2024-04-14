from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import BaseUserCreationForm
from django.core import validators

from users import models


class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}),
                               validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(10)])

    def clean_email(self):
        # validation
        # transformation
        email = self.cleaned_data.get('email')
        # raise forms.ValidationError('Email Is Invalid')
        return email.lower()

    def clean(self):
        # cleaned_data = self.cleaned_data
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            self.user = user
        else:
            raise forms.ValidationError('Invalid Username or Password')

    def get_user(self):
        return self.user


class UserSignupForm(BaseUserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for bound_field in self.visible_fields():
            if bound_field.field.widget.attrs.get('class'):
                bound_field.field.widget.attrs['class'] += ' form-control'
            else:
                bound_field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        # model = models.User # get_user_model()
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "dob")
        # exclude = ("last_login", "password", "date_joined")
