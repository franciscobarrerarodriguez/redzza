from registration.forms import RegistrationForm
from django import forms
 
class ExRegistrationForm(RegistrationForm):
    is_staff = forms.ChoiceField(label = "Eres un cliente?:")