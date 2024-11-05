from pyexpat.errors import messages

from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, get_object_or_404

from GestionAbsence.forms import loginForm, EtudiantForm, AbsenceForm
from GestionAbsence.models import Etudiant, Absence


# Create your views here.

def home(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):  # Utilisation d'un nom différent pour éviter le conflit avec django.contrib.auth.login
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Spécifiez l'utilisateur ici
                return redirect('liste_etudiants')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})


def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'ajouter_etudiant.html', {'form': form})


def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    etudiant.delete()
    return redirect('liste_etudiants')


def ajouter_absence(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            absence.etudiant = etudiant
            absence.save()
            return redirect('liste_etudiants')
    else:
        form = AbsenceForm()
    return render(request, 'ajouter_absence.html', {'form': form, 'etudiant': etudiant})


def supprimer_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    absence.delete()
    return redirect('liste_etudiants')
