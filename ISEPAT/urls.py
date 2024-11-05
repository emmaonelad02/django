"""
URL configuration for ISEPAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from GestionAbsence import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiants/<int:etudiant_id>/ajouter_absence/', views.ajouter_absence, name='ajouter_absence'),
    path('absences/<int:absence_id>/supprimer/', views.supprimer_absence, name='supprimer_absence'),
]
