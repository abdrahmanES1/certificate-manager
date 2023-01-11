# Create your models here.
from django.db import models
from django.contrib import admin

# Create your models here.

class Filiere(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nom



class Etudiant(models.Model):
    CNI = models.CharField(primary_key=True, max_length=10)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, verbose_name="filier")

    def __str__(self) -> str:
        return f"{self.CNI}, {self.nom}, {self.prenom}"





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
    num_classment = models.IntegerField()
    etudient = models.ForeignKey(Etudiant, on_delete=models.CASCADE, verbose_name="etudient")
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, verbose_name="filiere")
    type_diplome = models.ForeignKey(
        TypeDiplome, on_delete=models.CASCADE, verbose_name="type de diplome")
    statut = models.IntegerField(choices=satut_diplome_choices, default=0)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

    list_display = ["num_classment", "etudient"]
    def __str__(self) -> str:
        return f'{self.etudient.nom} |  {self.etudient.CNI} | {self.type_diplome.type} | {self.filiere.nom}'
    class Meta:
        unique_together = [('etudient', 'filiere', 'type_diplome',),
                           ('num_classment', 'filiere', 'type_diplome',)]

    
    def save(self, *args, **kwargs):
        if  not self.num_classment:
            last = Diplome.objects.filter(filiere_id=4, type_diplome_id=2).aggregate(models.Max('num_classment'))
            if last['num_classment__max'] is None:
                self.num_classment = 1
            else:
                self.num_classment = last['num_classment__max'] + 1

        super().save(*args, **kwargs)
    # def __str__(self) -> str:
    #     return f"{self.num_classment}, {self.etudient}, {self.filiere}, {self.type_diplome}"


