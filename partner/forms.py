from django import forms
from django.contrib.auth.models import User
from . import models


class PartnerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {'password': forms.PasswordInput()}


class PartnerForm(forms.ModelForm):
    class Meta:
        model = models.Partner
        fields = ['address', 'mobile']

