from django.contrib import admin
from .models import Diplome,  Etudiant, TypeDiplome, Filiere
from import_export.admin import ImportExportMixin, ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import resources
from import_export.fields import Field

class BookResource(resources.ModelResource):
    num_classment = Field(attribute='num_classment',
                          column_name='Numero de classement')
    etudient_nom = Field(attribute='etudient__nom', column_name='Nom')
    etudient_prenom = Field(attribute='etudient__prenom', column_name='Prenom')
    filiere = Field(attribute='filiere__nom', column_name='Filière')
    type_dilome = Field(attribute='type_diplome__type',
                        column_name='Types de diplôme')
    class Meta:
        model = Diplome
        fields = ('num_classment', 'etudient_nom', 'etudient_prenom','filiere', 'type_dilome',)


class FiliereAdmin(admin.ModelAdmin):
    model = Filiere
    list_display = ["nom"]
    search_fields = ["nom"]


class DiplomeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    model = Diplome
    list_display = ['num_classment', 'etudient',
                    'filiere', 'type_diplome', 'statut', ]
    ordering = ['num_classment', ]
    search_fields = ('etudient__CNI',)
    list_filter = ('type_diplome', 'filiere', 'createdAt')
    resource_classes = [BookResource]
    list_per_page = 10
    ordering = ('-createdAt',)
    # @admin.action(description='print')
    # def print_list_diplome(DiplomeAdmin, request, queryset):
    #     return
    #     queryset.update(type_diplome=1)
    # actions = (print_list_diplome,)


class DiplomeInline(admin.TabularInline):
    model = Diplome
    fields = ['filiere', 'type_diplome', 'statut', ]
    extra = 2


class EtudiantAdmin(admin.ModelAdmin):
    model = Etudiant
    list_display = ["CNI", "nom", 'prenom', 'filiere']
    search_fields = ["CNI", "nom"]
    list_filter = ["filiere"]
    inlines = [DiplomeInline]
    list_per_page = 10


admin.site.register(Diplome, DiplomeAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(TypeDiplome)
admin.site.register(Filiere, FiliereAdmin)
# admin.site.site_header = "Admin Panel"
# admin.site.site_title = "Admin Panel"


