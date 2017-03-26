from registration.forms import RegistrationForm
from django import forms


class ProfileForm(RegistrationForm):
    # avatar = forms.ImageField()
    location = forms.CharField()
    # birth_date = forms.DateField()
