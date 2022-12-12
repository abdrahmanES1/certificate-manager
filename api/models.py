from django.db import models
from django.contrib import admin

# Create your models here.
from django.db import models
# from .validators import validate_file_excel_extension
# Create your models here.

class Filiere(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nom


class FiliereAdmin(admin.ModelAdmin):
    model = Filiere
    list_display =  ["nom"]
    search_fields = ["nom"]

class Etudiant(models.Model):
    CNI = models.CharField(primary_key=True, max_length=10)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, verbose_name="filier")

    def __str__(self) -> str:
        return f"{self.CNI}, {self.nom}, {self.prenom}"

class EtudiantAdmin(admin.ModelAdmin):
    model = Etudiant
    list_display = ["CNI", "nom", 'prenom', 'filiere']
    search_fields = ["CNI", "nom"]
    list_filter = ["filiere"]


class TypeDiplome(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.type}"


satut_diplome_choices = [
    (0, "Dossier Déposé"),
    (1, "Dossier En Cour De Traitement"),
    (3, "Diplome En Cour De Signature"),
    (4, "Diplôme Prêt Pour Retrait")
]


class Diplome(models.Model):
    num_classment = models.IntegerField(auto_created=True)
    etudient = models.ForeignKey(Etudiant, on_delete=models.CASCADE, verbose_name="etudient")
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, verbose_name="filiere")
    type_diplome = models.ForeignKey(
        TypeDiplome, on_delete=models.CASCADE, verbose_name="type de diplome")
    statut = models.IntegerField(choices=satut_diplome_choices, default=0)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

    list_display = ["num_classment", "etudient"]

    class Meta:
        unique_together = ('etudient', 'filiere', 'type_diplome',)
        
    # def __str__(self) -> str:
    #     return f"{self.num_classment}, {self.etudient}, {self.filiere}, {self.type_diplome}"


# @admin.action(description='test action')
# def make_publication(DiplomeAdmin, request, queryset):
#     queryset.update(type_diplome=1)

class DiplomeAdmin(admin.ModelAdmin):
    model = Diplome
    list_display = ['num_classment', 'etudient', 'filiere', 'type_diplome', 'statut',]
    ordering = ['num_classment',]
    search_fields = ('num_classment', )
    list_filter = ('type_diplome', 'filiere', 'createdAt')
    # actions = (make_publication,)





