from django.db import models
from django.conf import settings
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin: {self.user.username}"


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="absences")
    date_absence = models.DateField()

    def __str__(self):
        return f"Absence de {self.etudiant} le {self.date_absence}"


