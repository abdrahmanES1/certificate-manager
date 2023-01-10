from django.contrib.auth.models import User
from django.shortcuts import render
from urllib.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Diplome, Filiere, TypeDiplome
from .serializers import diplome_serializer, filiere_serializer, type_diplome_serializer
from rest_framework import mixins

# Create your views here.
from rest_framework import generics


class DiplomeList(generics.ListCreateAPIView):
    queryset = Diplome.objects.all().prefetch_related()
    serializer_class = diplome_serializer


class DiplomeList(generics.ListCreateAPIView):
    queryset = Diplome.objects.all().prefetch_related()
    serializer_class = diplome_serializer

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class DiplomeDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Diplome.objects.all()
    serializer_class = diplome_serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



@api_view(['GET'])
def search(request:Request, CNI):
    # if request.method == "GET":
    try:
        qs = Diplome.objects.get(etudient=CNI)
        queryset = diplome_serializer(qs)
        return Response(queryset.data)
    except Diplome.DoesNotExist:
        return Response({"message": f"CNI : {CNI} Not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_filiere(request: Request):
    qs = Filiere.objects.all()
    queryset = filiere_serializer(qs, many=True)
    return Response(queryset.data)


@api_view(['GET'])
def get_all_type_diplome(request: Request):
    qs = TypeDiplome.objects.all()
    queryset = type_diplome_serializer(qs, many=True)
    return Response(queryset.data)


@api_view(['GET'])
def search_by(request: Request,  CNI, filiere, type_diplome):
    try:
        qs = Diplome.objects.get(
            etudient=CNI, filiere=filiere, type_diplome=type_diplome)
        queryset = diplome_serializer(qs)
        print(request.user.is_superuser)
        return Response(queryset.data)
    except Diplome.DoesNotExist:
        return Response({"message": f"CNI : {CNI} Not found"}, status=status.HTTP_404_NOT_FOUND)

