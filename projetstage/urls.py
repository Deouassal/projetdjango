from django.urls import path, include
from django.contrib import admin
from . import views
from .views import register,  inscription_succes
from .views import inscription_admin, connexion_admin, deconnexion_utilisateur, deconnexion_admin
from .views import list_materiels_informatiques
#from .views import list_consommables
from .views import list_equipements, liste_equipements_utilisateur
from .views import liste_equipements, liste_materiel_informatique, liste_affectations, liste_consommables, liste_fournisseurs, affectation
from .views import home 


#from projetstage.views import login_user
#from django.contrib.auth.views import LoginView # Importez la vue LoginView
#from .views import vueLoginView


urlpatterns = [
    #path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('équipements/', views.équipements,name='équipements'),
    #path('consommables/', views.consommables, name='consommables'),
    path('materiels_informatiques/', views.materiels_informatiques, name='materiels_informatiques'),
    path('', views.home, name='home'),
    path('inscription/', register, name='inscription'),
    path('inscription_succes/', inscription_succes, name='inscription_succes'),
    path('inscription admin/', views.inscription_admin, name='inscription_admin'),
    path('connexion_admin/', views.connexion_admin, name='connexion_admin'),
    #path('administrateur/materiels-informatiques/', list_materiels_informatiques, name='list_materiels_informatiques'),
    #path('administrateur/consommables/', list_consommables, name='list_consommables'),
    path('administrateur/equipements/', list_equipements, name='list_equipements'),
    #path('administrateur/', index_admin, name='index_admin'),
    path('equipements/ajouter/', views.ajouter_equipement, name='ajouter_equipement'),
    path('fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('equipements/', liste_equipements, name='liste_equipements'),
    path('ajouter_consommable/', views.ajouter_consommable, name='ajouter_consommable'),
    #path('ajouter_materiel_informatique/', views.ajouter_materiel_informatique, name='ajouter_materiel_informatique'),
    path('consommables/', views.liste_consommables, name='liste_consommables'),
    path('enregistrer_commande/', views.enregistrer_commande, name='enregistrer_commande'),
    path('liste_commandes/', views.liste_commandes, name='liste_commandes'),
    #path('affecter_equipement/<int:demande_id>/', views.affecter_equipement, name='affecter_equipement'),
    #path('affectations/', views.affectations, name='affectations'),
    path('demander_equipement/', views.demander_equipement, name='demander_equipement'),
    path('liste_demandes/', views.liste_demandes, name='liste_demandes'),
    path('materiel_informatique/', views.liste_materiel_informatique, name='liste_materiel_informatique'),
    path('materiel_informatique/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('equipements/<int:id_equipement>/modifier/', views.modifier_equipement, name='modifier_equipement'),
    path('equipements/<int:id_equipement>/supprimer/', views.supprimer_equipement, name='supprimer_equipement'),
    path('modifier_materiel_informatique/<int:id_materiel_informatique>/modifier/', views.modifier_materiel_informatique, name='modifier_materiel_informatique'),
    path('supprimer_materiel_informatique/<int:id_materiel_informatique>/supprimer/', views.supprimer_materiel_informatique, name='supprimer_materiel_informatique'),
    path('consommables/', views.liste_consommables, name='liste_consommables'),
    path('consommables/<int:id_consommable>/modifier/', views.modifier_consommable, name='modifier_consommable'),
    path('consommables/<int:id_consommable>/supprimer/', views.supprimer_consommable, name='supprimer_consommable'),
    path('demandes/<int:id_demande>/modifier/', views.modifier_demande, name='modifier_demande'),
    path('demandes/<int:id_demande>/supprimer/', views.supprimer_demande, name='supprimer_demande'),
    #path('connexion/', views.vue_connexion, name='connexion'),
    #path('deconnexion/', views.vue_deconnexion, name='deconnexion'),
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    #path('home/', home, name='home'),
    #path('login/', vueLoginView.as_view(), name='login'),
    #path('login/', views.login_user, name='login'),
    #path('login/', login_view, name='login'),
    #path('login/', include('login.urls')),
    #path('login/', views.user_login, name='login'),
    path('login/', views.login, name='login'),
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'),
    #path('deconnexion/', deconnexion, name='deconnexion'),
    path('modifier_commande/<int:id_commande>/', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<int:id_commande>/', views.supprimer_commande, name='supprimer_commande'),
    path('utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('fournisseurs/<int:id_fournisseur>/modifier/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('fournisseurs/<int:id_fournisseur>/supprimer/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    path('fournisseurs/ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('tableau-de-bord/', views.tableau_de_bord_utilisateur, name='tableau_de_bord_utilisateur'),
    #path('deconnexion/', views.deconnexion_utilisateur, name='deconnexion_utilisateur'),
    path('deconnexion_utilisateur/', views.deconnexion_utilisateur, name='deconnexion_utilisateur'),
    path('deconnexion_admin/', views.deconnexion_admin, name='deconnexion_admin'),
    path('affectations/', views.liste_affectations, name='liste_affectations'),
    path('affectations/ajouter/', views.affectation, name='ajouter_affectation'),
    path('affectations/modifier/<int:id_affectation>/', views.modifier_affectation, name='modifier_affectation'),
    path('affectations/supprimer/<int:id_affectation>/', views.supprimer_affectation, name='supprimer_affectation'),
    path('listes_equipements_utilisateur/', views.liste_equipements_utilisateur, name='liste_equipements_utilisateur'),

    ]








