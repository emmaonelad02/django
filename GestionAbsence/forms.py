from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from twisted.mail.smtp import User

from GestionAbsence.models import Etudiant, Absence


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'matricule']


class AbsenceForm(forms.ModelForm):
    date_absence = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Absence
        fields = ['date_absence']


class loginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur',
        }),
        label='Nom d\'utilisateur'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe',
        }),
        label='Mot de passe'
    )
