from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class role(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom
    
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdetail')
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    
    
class localites(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom
    
    

class adresse(models.Model):
    position = models.CharField(max_length=50)
    localite = models.ForeignKey(localites, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class consomateurs(models.Model):
    preference = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Commandes(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_command = models.CharField(max_length=50)
    statut = models.IntegerField()
    date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.numero_command

class moyen_payement(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom

class Facture(models.Model):
    commandes = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    moyen_de_payement = models.ForeignKey(moyen_payement, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Facture pour {self.commandes.numero_command}"
    

class livreur(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom


class ligne_de_livraison(models.Model):
    numero_livreur = models.ForeignKey(livreur, on_delete=models.CASCADE)
    reference_livreur = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    quantite_livre = models.IntegerField()
    statut_livraison = models.IntegerField()
    
    
class marchand(models.Model):
    certifie = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class categories(models.Model):
    nom = models.CharField(max_length=50)
    categorie_parent = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom
    
class images(models.Model):
    url = models.CharField(max_length=10000)
    def __str__(self) -> str:
        return self.url
    
class produit(models.Model):
    nom = models.CharField(max_length=50)
    quantite = models.IntegerField()
    description = models.CharField(max_length=500)
    prix = models.IntegerField()
    categorie = models.ForeignKey(categories, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(images, on_delete=models.CASCADE)
    date_ajout = models.DateField(auto_now=True)
    
    
    
class ligne_de_commande(models.Model):
    reference_produit = models.ForeignKey(produit, on_delete=models.CASCADE)
    numero_commande = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    quantite_commande = models.IntegerField()
    statut = models.IntegerField()
    