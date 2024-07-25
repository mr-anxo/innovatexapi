from rest_framework import routers
from .views import (
    adresseViewset, 
    roleViewset, 
    localitesViewset, 
    # UserDetailViewset, 
    CommandesViewset, 
    FactureViewset, 
    moyen_payementViewset, 
    consomateursViewset,
    categoriesViewset,
    imagesViewset,
    livreurViewset,
    produitViewset,
    ligne_de_commandeViewset,
    ligne_de_livraisonViewset,
    marchandViewset,
    UserViewset
)
router = routers.DefaultRouter()

router.register('Comptes', UserViewset)
router.register('role', roleViewset)
router.register('adresse', adresseViewset)
router.register('localities', localitesViewset)
# router.register('UserDetail', UserDetailViewset)
router.register('Commandes', CommandesViewset)
router.register('facture', FactureViewset)
router.register('moyen_de_payement', moyen_payementViewset)
router.register('consomateurs', consomateursViewset)
router.register('categories', categoriesViewset)
router.register('images', imagesViewset)
router.register('livreur', livreurViewset)
router.register('produit', produitViewset)
router.register('marchand', marchandViewset)
router.register('ligne_de_livraison', ligne_de_livraisonViewset)
router.register('ligne_de_commande', ligne_de_commandeViewset)