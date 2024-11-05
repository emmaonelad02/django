from django.contrib import admin

from GestionAbsence.models import Etudiant, Admin, Absence

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Admin)
admin.site.register(Absence)
