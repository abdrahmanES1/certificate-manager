from rest_framework import serializers
from .models import Diplome, Etudiant, Filiere, TypeDiplome

class etudiant_serializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['CNI', 'nom', 'prenom']

class diplome_serializer(serializers.ModelSerializer):
    etudient = serializers.StringRelatedField(read_only=True)
    filier = serializers.StringRelatedField(read_only=True)
    type_diplome = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Diplome
        fields = ['id', 'num_classment', 'etudient', 'filier', 'type_diplome', 'createdAt']


class filiere_serializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ['id', 'nom']


class type_diplome_serializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDiplome
        fields = ['id', 'type']
