from django import forms
from django.contrib.auth import authenticate


# Form para el inicio de sesion a la plataforma, se realiza mediante correo y contraseña
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email=email, password=password)

        if self.user_cache is None:
            raise forms.ValidationError('Incorrect user')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Inactive User')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
