from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='')  # ← help_text vide

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Supprime tous les messages d'aide
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None