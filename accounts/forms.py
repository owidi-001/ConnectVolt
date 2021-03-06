from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
from django.db.models import fields

from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', "email")