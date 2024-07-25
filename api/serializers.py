from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    role, 
    adresse, 
    localites, 
    Commandes, 
    moyen_payement, 
    UserDetail, 
    Facture, 
    consomateurs, 
    categories, 
    images, 
    livreur, 
    produit, 
    marchand, 
    ligne_de_livraison, 
    ligne_de_commande

)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['role', 'contact']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    userdetail = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'userdetail')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        userdetail_data = validated_data.pop('userdetail')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        UserDetail.objects.create(
            user=user,
            role=userdetail_data['role'],
            contact=userdetail_data['contact']
        )
        return user



        
        
class roleSerialiser(serializers.ModelSerializer):
    class Meta:
        model= role
        fields= '__all__'
        
        
class adresseSerialiser(serializers.ModelSerializer):
    class Meta:
        model= adresse
        fields= ['position']
        
        
class localitesSerialiser(serializers.ModelSerializer):
    class Meta:
        model= localites
        fields= '__all__'
        
class CommandesSerialiser(serializers.ModelSerializer):
    class Meta:
        model= Commandes
        fields= '__all__'
        
class moyen_payementSerialiser(serializers.ModelSerializer):
    class Meta:
        model= moyen_payement
        fields= '__all__'
        
        
class FactureSerialiser(serializers.ModelSerializer):
    class Meta:
        model= Facture
        fields= '__all__'
        
class consomateursSerialiser(serializers.ModelSerializer):
    class Meta:
        model= consomateurs
        fields= '__all__'
        
        
        
        
class categoriesSerialiser(serializers.ModelSerializer):
    class Meta:
        model= categories
        fields= '__all__'
        
        
        
        
class imagesSerialiser(serializers.ModelSerializer):
    class Meta:
        model= images
        fields= '__all__'
        
        
        
        
class livreurSerialiser(serializers.ModelSerializer):
    class Meta:
        model= livreur
        fields= '__all__'
        
        
        
        
class produitSerialiser(serializers.ModelSerializer):
    class Meta:
        model= produit
        fields= '__all__'
        
        
        
        
class marchandSerialiser(serializers.ModelSerializer):
    class Meta:
        model= marchand
        fields= '__all__'
        
        
        
        
class ligne_de_livraisonSerialiser(serializers.ModelSerializer):
    class Meta:
        model= ligne_de_livraison
        fields= '__all__'
        
        
        
        
class ligne_de_commandeSerialiser(serializers.ModelSerializer):
    class Meta:
        model= ligne_de_commande
        fields= '__all__'
        
        
        
        
        