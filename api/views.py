from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import (
    role, 
    adresse, 
    localites, 
    Commandes, 
    moyen_payement, 
    # UserDetail, 
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
from .serializers import (
    roleSerialiser, 
    adresseSerialiser, 
    localitesSerialiser, 
    CommandesSerialiser, 
    moyen_payementSerialiser, 
    # UserDetailSerialiser, 
    FactureSerialiser, 
    consomateursSerialiser,
    categoriesSerialiser,
    imagesSerialiser,
    livreurSerialiser,
    produitSerialiser,
    marchandSerialiser,
    ligne_de_livraisonSerialiser,
    ligne_de_commandeSerialiser,
    UserSerializer
)
# Create your views here.

class roleViewset(viewsets.ModelViewSet):
    queryset = role.objects.all()
    serializer_class= roleSerialiser
    
class adresseViewset(viewsets.ModelViewSet):
    queryset= adresse.objects.all()
    serializer_class= adresseSerialiser
    permission_classes= [IsAuthenticated]
    
class localitesViewset(viewsets.ModelViewSet):
    queryset= localites.objects.all()
    serializer_class= localitesSerialiser
    permission_classes= [IsAuthenticated]
    
class CommandesViewset(viewsets.ModelViewSet):
    queryset= Commandes.objects.all()
    serializer_class= CommandesSerialiser
    
class moyen_payementViewset(viewsets.ModelViewSet):
    queryset= moyen_payement.objects.all()
    serializer_class= moyen_payementSerialiser
    
class consomateursViewset(viewsets.ModelViewSet):
    queryset= consomateurs.objects.all()
    serializer_class= consomateursSerialiser
    
class FactureViewset(viewsets.ModelViewSet):
    queryset= Facture.objects.all()
    serializer_class= FactureSerialiser
    
# class UserDetailViewset(viewsets.ModelViewSet):
#     queryset= UserDetail.objects.all()
#     serializer_class= UserDetailSerialiser
    
class categoriesViewset(viewsets.ModelViewSet):
    queryset= categories.objects.all()
    serializer_class= categoriesSerialiser
    
class imagesViewset(viewsets.ModelViewSet):
    queryset= images.objects.all()
    serializer_class= imagesSerialiser
    
class livreurViewset(viewsets.ModelViewSet):
    queryset= livreur.objects.all()
    serializer_class= livreurSerialiser
    
class produitViewset(viewsets.ModelViewSet):
    queryset= produit.objects.all()
    serializer_class= produitSerialiser
    
class ligne_de_livraisonViewset(viewsets.ModelViewSet):
    queryset= ligne_de_livraison.objects.all()
    serializer_class= ligne_de_livraisonSerialiser
    
class ligne_de_commandeViewset(viewsets.ModelViewSet):
    queryset= ligne_de_commande.objects.all()
    serializer_class= ligne_de_commandeSerialiser
    
class marchandViewset(viewsets.ModelViewSet):
    queryset= marchand.objects.all()
    serializer_class= marchandSerialiser
    
class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    
