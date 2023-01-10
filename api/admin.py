from django.contrib import admin
from .models import Diplome, DiplomeAdmin, Etudiant, EtudiantAdmin, TypeDiplome, Filiere, FiliereAdmin
# Register your models here.
admin.site.register(Diplome, DiplomeAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(TypeDiplome)
admin.site.register(Filiere, FiliereAdmin)
# admin.site.site_header = "Admin Panel"
# admin.site.site_title = "Admin Panel"


