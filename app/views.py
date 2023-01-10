from django.shortcuts import render
from urllib.request import Request
from api.models import Filiere, Diplome, Etudiant, TypeDiplome, satut_diplome_choices
# Create your views here.
from django.db.models import Max

def index(request: Request):
    ctx = {'filieres': Filiere.objects.all(), 'type_diplomes': TypeDiplome.objects.all(
    ), 'satut_diplome_choices': satut_diplome_choices, 'maxid':  Diplome.objects.filter(filiere_id=4, type_diplome_id=2).aggregate(Max('num_classment'))}
    ctx['authenticated'] = request.user.is_authenticated
    if request.method == 'POST':
        CNI = request.POST.get('CNI')
        filiere = request.POST.get('filiere')
        diplome = request.POST.get('diplome')
        try:
            qs = Diplome.objects.get(filiere=filiere, type_diplome=diplome, etudient=CNI)
            ctx['diplome'] = qs
            
        except Diplome.DoesNotExist:
            ctx['error'] = 'not found'
    
    return render(request, 'app/index.html', ctx)
