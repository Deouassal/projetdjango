from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm , ConnexionForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from projetstage.models import administrateur
from .forms import AjouterEquipementForm, CommandeForm, ModifierDemandeForm
from .models import Fournisseurs
from .forms import FournisseurForm
from .models import Utilisateurs
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import forms
from .forms import InscriptionAdminForm, ConsommablesForm, SupprimerConsommableForm, DemandeForm, SupprimerDemandeForm, InscriptionAdminForm
#from django.contrib.auth.decorators import login_required
from .models import Consommables, Commande, Affectations, Demandes , administrateur
from .models import Equipements , Materiels_Informatiques
from .forms import AffectationForm, DemandeForm, AjouterConsommableForm,EquipementForm, SupprimerMaterielInformatiqueForm, MaterielsInformatiquesForm,  UtilisateursLoginForm
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import check_password, make_password
from datetime import datetime
from .forms import FournisseurForm , ModifierFournisseurForm, ModifierAffectationForm, AjouterMaterielInformatiqueForm
from django.urls import reverse



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['mot_de_passe'])
            user.save()
            return redirect('inscription_succes')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

#@login_required
def home(request):
    return render(request, 'home.html')


def équipements(request):
    # Code pour afficher la page des équipements
    return render(request, 'equipements.html')


#def consommables(request):
    # Code pour récupérer les consommables depuis la base de données
    #consommables = Consommable.objects.all()

    #context = {
       # 'consommables': #consommables,
    #}
    #return render(request, 'consommables.html', context)

def materiels_informatiques(request):
    # Code pour récupérer les matériels informatiques depuis la base de données
    materiels = Materiel.objects.all()

    context = {
        'materiels': materiels,
    }
    return render(request, 'materiels_informatiques.html', context)



    
def inscription_succes(request):
    return render(request, 'inscription_succes.html')




#def connexion_admin(request):
 #   if request.method == 'POST':
  #      form = AuthenticationForm(request, data=request.POST)
   #     if form.is_valid():
    #        username = form.cleaned_data.get('username')
     #       password = form.cleaned_data.get('password')
      #      user = authenticate(username=username, password=password)
       #     if user is not None:
        #        login(request, user)
         #       return redirect('admin_index')
    #else:
     #   form = AuthenticationForm()

    #context = {
     #   'form': form,
    #}

    #return render(request, 'connexion_admin.html', context)

#def index_admin(request):
 #   return render(request, 'admin_index.html')

def list_equipements(request):
    equipements = Equipements.objects.all()
    return render(request, 'admin_equipements.html', {'equipements': equipements})

#def list_consommables(request):
    #consommables = Consommable.objects.all()
    #return render(request, 'admin_consommables.html', {'consommables': consommables})

def list_materiels_informatiques(request):
    materiels_informatiques = MaterielInformatique.objects.all()
    return render(request, 'admin_materiels_informatiques.html', {'materiels_informatiques': materiels_informatiques})

# vue pour ajouter un consommable
def ajouter_consommable(request):
    if request.method == 'POST':
        form = AjouterConsommableForm(request.POST)
        if form.is_valid():
            consommable = form.save(commit=False)
            consommable.save()
            url_liste_consommables = reverse('liste_consommables')
            url_liste_consommables_utilisateur = reverse('liste_consommables_utilisateur')
            return redirect(url_liste_consommables, url_liste_consommables_utilisateur)
    else:
        form = AjouterConsommableForm()
    context = {'form': form}
    return render(request, 'ajouter_consommable.html', context)

# 

def liste_consommables_utilisateur(request):
    consommables = Consommables.objects.filter()
    context = {'consommables': consommables}
    return render(request, 'liste_consommables_utilisateur.html', context)

#

def equipements(request):
    equipements = Equipement.objects.all()
    return render(request, 'admin_equipements.html', {'equipements': equipements})


def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save(commit=False)
            fournisseur.telephone = form.cleaned_data['telephone']
            fournisseur.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'ajouter_fournisseur.html', {'form': form})

def liste_fournisseurs(request):
    fournisseurs = Fournisseurs.objects.all()
    return render(request, 'liste_fournisseurs.html', {'fournisseurs': fournisseurs})

def liste_equipements(request):
    equipements = Equipements.objects.all()
    return render(request, 'liste_equipements.html', {'equipements': equipements})

def liste_consommables(request):
    consommables = Consommables.objects.all()
    return render(request, 'liste_consommables.html', {'consommables': consommables})
def liste_materiel_informatique(request):
    materiels_informatiques = Materiels_Informatiques.objects.all()
    return render(request, 'liste_materiel_informatique.html', {'materiels_informatiques': materiels_informatiques})
def liste_equipements_utilisateur(request):
    equipements = Equipements.objects.filter()
    context = {'equipements': equipements}
    return render(request, 'equipements_utilisateur.html', context)

#def liste_materiels_utilisateur(request):
 #   materiels_informatiques = Materiels_Informatiques.objects.filter()
  #  context = {'materiels_informatiques': materiels_informatiques}
   # return render(request, 'materiels_utilisateur.html', context) 


def liste_materiels_utilisateur(request):
    materiels_informatiques = Materiels_Informatiques.objects.all()
    context = {'materiels_informatiques': materiels_informatiques}
    return render(request, 'liste_materiels_utilisateur.html', context)

# Ajout équipement

def ajouter_equipement(request):
    if request.method == 'POST':
        form = AjouterEquipementForm(request.POST)
        if form.is_valid():
            equipement = form.save(commit=False)
            equipement.utilisateur = request.user
            equipement.statut = 'En stock'
            equipement.save()
            url_liste_equipements = reverse('liste_equipements')
            url_liste_equipements_utilisateur = reverse('liste_equipements_utilisateur')
            return redirect(url_liste_equipements, url_liste_equipements_utilisateur)
    else:
        form = AjouterEquipementForm()
    context = {'form': form}
    return render(request, 'ajouter_equipement.html', context)
# vue pour ajouter un matériel informatique

def ajouter_materiel(request):
    if request.method == 'POST':
        form = AjouterMaterielInformatiqueForm(request.POST)
        if form.is_valid():
            materiel = form.save(commit=False)
            materiel.save()
            url_liste_materiels_informatiques = reverse('liste_materiels_informatiques')
            url_liste_materiels_utilisateur = reverse('liste_materiels_utilisateur')
            return redirect(url_liste_materiels_informatiques, url_liste_materiels_utilisateur)
    else:
        form = AjouterMaterielInformatiqueForm()
    context = {'form': form}
    return render(request, 'ajouter_materiel_informatique.html', context)


# Vue enregistrer commande 
def enregistrer_commande(request):
    if request.method == 'POST':
        date_commande = request.POST['date_commande']
        articles_commandes = request.POST['articles_commandes']
        quantite_commandee = request.POST['quantite_commandee']
        statut_commande = request.POST['statut_commande']
        id_fournisseur = request.POST.get('id_fournisseur')
        date_livraison_prevue = request.POST['date_livraison_prevue']
        #date_livraison_reelle = request.POST['date_livraison_reelle']
        #try:
         #   date_livraison_reelle = datetime.strptime(date_livraison_reelle, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        #except ValueError:

    # La date n'a pas le format attendu
           #date_livraison_reelle = None
        id_equipement = request.POST.get('id_equipement')
        id_consommable = request.POST.get('id_consommable')
        id_materiel_informatique = request.POST.get('id_materiel_informatique')

        if id_fournisseur and id_fournisseur.strip().isdigit():
            fournisseur = Fournisseurs.objects.get(pk=int(id_fournisseur))
        else:
            fournisseur = None

        if id_equipement and id_equipement.strip().isdigit():
            equipement = Equipements.objects.get(pk=int(id_equipement))
        else:
            equipement = None

        if id_consommable and id_consommable.strip().isdigit():
            consommable = Consommables.objects.get(pk=int(id_consommable))
        else:
            consommable = None

        if id_materiel_informatique and id_materiel_informatique.strip().isdigit():
            materiel_informatique = Materiels_Informatiques.objects.get(pk=int(id_materiel_informatique))
        else:
            materiel_informatique = None

        commande = Commande(
            date_commande=date_commande,
            articles_commandes=articles_commandes,
            quantite_commandee=quantite_commandee,
            statut_commande=statut_commande,
            id_fournisseur=fournisseur,
            date_livraison_prevue=date_livraison_prevue,
            id_equipement=equipement,
            id_consommable=consommable,
            id_materiel_informatique=materiel_informatique
        )
        commande.save()

        return redirect('liste_commandes')
    else:
        fournisseurs = Fournisseurs.objects.all()
        equipements = Equipements.objects.all()
        consommables = Consommables.objects.all()
        materiels_informatiques = Materiels_Informatiques.objects.all()
        context = {'fournisseurs': fournisseurs, 'equipements': equipements, 'consommables': consommables, 'materiels_informatiques': materiels_informatiques}
        return render(request, 'enregistrer_commande.html', context)

#vue liste commande 
def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'liste_commandes.html', {'commandes': commandes})

 
# 
def demander_equipement(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            demande = form.save()
            url_liste_demandes = reverse('liste_demandes')
            url_liste_demandes_utilisateur = reverse('liste_demandes_utilisateur')
            if demande.equipement.utilisateur == request.user:
                return redirect(url_liste_demandes_utilisateur)
            else:
                return redirect(url_liste_demandes)
    else:
        form = DemandeForm()
    return render(request, 'demander_equipement.html', {'form': form})

#
def liste_demandes_utilisateur(request):
    # Récupérer les demandes d'équipement associées à l'utilisateur connecté
    demandes_equipement = Demandes.objects.filter()
    context = {'demandes_equipement': demandes_equipement}
    return render(request, 'liste_demandes_utilisateur.html', context)


#
def liste_demandes(request):
    demandes = Demandes.objects.all()
    return render(request, 'liste_demandes.html', {'demandes': demandes})

#
#def liste_demandes(request):
 #   demandes = Demandes.objects.all()
  #  return render(request, 'liste_demandes.html', {'demandes': demandes})


#def update_affectation(request, affectation_id):
 #   affectation = Affectation.objects.get(pk=affectation_id)
  #  if request.method == 'POST':
   #     form = AffectationUpdateForm(request.POST, instance=affectation)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('liste_affectations')
    #else:
     #   form = AffectationUpdateForm(instance=affectation)
    #return render(request, 'update_affectation.html', {'form': form})


# vue pour modification 

def modifier_equipement(request, id_equipement):
    equipement = get_object_or_404(Equipements, id_equipement=id_equipement)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('liste_equipements')
    else:
        form = EquipementForm(instance=equipement)
    context = {'form': form}

    return render(request, 'modifier_equipement.html', context)

# vue suppresion 
def supprimer_equipement(request, id_equipement ):
    equipement = get_object_or_404(Equipements, id_equipement=id_equipement)
    if request.method == 'POST':
        equipement.delete()
        return redirect('liste_equipements')
    context = {'equipement': equipement}
    return render(request, 'supprimer_equipement.html', context)

# vue de modification pour Materiels_Informatiques
def modifier_materiel_informatique(request, id_materiel_informatique):
    materiel_informatique = get_object_or_404(Materiels_Informatiques, id_materiel_informatique=id_materiel_informatique)
    if request.method == 'POST':
        form = MaterielsInformatiquesForm(request.POST, instance=materiel_informatique)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel_informatique')
    else:
        form = MaterielsInformatiquesForm(instance=materiel_informatique)
    context = {'form': form}
    return render(request, 'modifier_materiel_informatique.html', context)

# vue de suppression pour Materiels_Informatiques
def supprimer_materiel_informatique(request, id_materiel_informatique):
    materiel_informatique = get_object_or_404(
        Materiels_Informatiques, id_materiel_informatique=id_materiel_informatique)

    if request.method == 'POST':
        materiel_informatique.delete()
        return redirect('liste_materiel_informatique')

    context = {'materiel_informatique': materiel_informatique}
    return render(request, 'supprimer_materiel_informatique.html', context)

# vue pour modification d'un consommable
def modifier_consommable(request, id_consommable):
    consommable = get_object_or_404(Consommables, id_consommable=id_consommable)
    if request.method == 'POST':
        form = ConsommablesForm(request.POST, instance=consommable)
        if form.is_valid():
            form.save()
            return redirect('liste_consommables')
    else:
        form = ConsommablesForm(instance=consommable)
    context = {'form': form}

    return render(request, 'modifier_consommable.html', context)


# vue pour suppression d'un consommable
def supprimer_consommable(request, id_consommable):
    consommable = get_object_or_404(Consommables, id_consommable=id_consommable)
    if request.method == 'POST':
        consommable.delete()
        return redirect('liste_consommables')

    context = {'consommable': consommable}
    return render(request, 'supprimer_consommable.html', context)

# 

def modifier_demande(request, id_demande):
    demande = get_object_or_404(Demandes, id_demande=id_demande)
    if request.method == 'POST':
        form = ModifierDemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('liste_demandes')
    else:
        form = ModifierDemandeForm(instance=demande)
    return render(request, 'modifier_demande.html', {'form': form, 'demande': demande})


def supprimer_demande(request, id_demande):
    demande = get_object_or_404(Demandes, id_demande=id_demande)
    if request.method == 'POST':
        supprimer_form = SupprimerDemandeForm(request.POST)
        if supprimer_form.is_valid() and supprimer_form.cleaned_data['confirm']:
            demande.delete()
            return redirect('liste_demandes')
    else:
        supprimer_form = SupprimerDemandeForm()
    return render(request, 'supprimer_demande.html', {'supprimer_form': supprimer_form, 'demande': demande})


#
#class vueLoginView(LoginView):
    #template_name = 'login.html'
    #fields = {'adresse_email': 'email', 'mot_de_passe': 'password'}


#def login_view(request):
    #if request.method == 'POST':
     #   form = LoginForm(request.POST)
      #  if form.is_valid():
       #     adresse_email = form.cleaned_data['adresse_email']
         #   mot_de_passe = form.cleaned_data['mot_de_passe']
          #  user = authenticate(request, username=adresse_email, password=mot_de_passe)
           # if user is not None:
            #    login(request, user)
             #   return redirect('home')
            #else:
             #   form.add_error(None, "L'adresse e-mail ou le mot de passe est incorrect.")
    #else:
     #   form = LoginForm()
    #return render(request, 'login.html', {'form': form})



#def login_view(request):
 #   if request.method == 'POST':
  #      form = AuthenticationForm(data=request.POST)
   #     if form.is_valid():
    #        username = form.cleaned_data.get('username')
     #       password = form.cleaned_data.get('password')
      #      user = authenticate(username=username, password=password)
       #     if user is not None:
        #        login(request, user)
         #       return redirect('home')
    #else:
     #   form = AuthenticationForm()
    #return render(request, 'login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        # Récupérer le nom d'utilisateur et le mot de passe soumis par l'utilisateur
        username = request.POST['username']
        password = request.POST['password']

        # Vérifier que le nom d'utilisateur et le mot de passe ne sont pas vides
        if username != '' and password != '':
            # Vérifier les informations d'identification de l'utilisateur dans la base de données
            try:
                utilisateur = Utilisateurs.objects.get(adresse_email=username)
                if check_password(password, utilisateur.mot_de_passe):
                    # Si les informations d'identification sont valides, connecter l'utilisateur et rediriger vers la liste des consommables
                    request.session['utilisateur_id'] = utilisateur.id_utilisateur
                    return redirect('tableau_de_bord_utilisateur')
            except Utilisateurs.DoesNotExist:
                pass
        
    # Si la méthode de la requête est GET, afficher simplement la page de connexion
    return render(request, 'login.html')

# vue pour la page de connexion de l'admin 

def inscription_admin(request):
    if request.method == 'POST':
        form = InscriptionAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion_admin')
    else:
        form = InscriptionAdminForm()

    context = {
        'form': form,
    }

    return render(request, 'inscription_admin.html', context)


# Connexion admin 

def connexion_admin(request):
    if request.method == 'POST':
        # Récupérer le nom d'utilisateur et le mot de passe soumis par l'utilisateur
        username = request.POST['username']
        password = request.POST['password']

        # Vérifier que le nom d'utilisateur et le mot de passe ne sont pas vides
        if username != '' and password != '':
            # Vérifier les informations d'identification de l'utilisateur dans la base de données
            try:
                user = administrateur.objects.get(adresse_email=username)
                if make_password(password, user.mot_de_passe):
                    # Si les informations d'identification sont valides, connecter l'utilisateur et rediriger vers la liste des consommables
                    request.session['id_administrateur'] = user.id_administrateur
                    return redirect('tableau_de_bord')
            except administrateur.DoesNotExist:
                pass
        
    # Si la méthode de la requête est GET, afficher simplement la page de connexion
    return render(request, 'connexion_admin.html')

# Vue tableau de bord 

def tableau_de_bord(request):
    # votre code pour le tableau de bord ici
    return render(request, 'tableau_de_bord.html')

def deconnexion_admin(request):
    logout(request)
    return redirect('connexion_admin')

#modification et suppression  de commandes 

def modifier_commande(request, id_commande):
    commande = get_object_or_404(Commande, id_commande=id_commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'modifier_commande.html', {'form': form})


# vue pour suppression d'une commande
def supprimer_commande(request, id_commande):
    commande = get_object_or_404(Commande, id_commande=id_commande)
    if request.method == 'POST':
        commande.delete()
        return redirect('liste_commandes')
    
    context = {'commande': commande}
    return render(request, 'supprimer_commande.html', context)

# vue liste utilisateurs 

def liste_utilisateurs(request):
    utilisateurs = Utilisateurs.objects.all()
    return render(request, 'liste_utilisateurs.html', {'utilisateurs': utilisateurs})

# vue pour modification d'un fournisseur
def modifier_fournisseur(request, id_fournisseur):
    fournisseur = get_object_or_404(Fournisseurs, id_fournisseur=id_fournisseur)
    form = ModifierFournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('liste_fournisseurs')
    context = {'form': form}
    return render(request, 'modifier_fournisseur.html', context)

# vue pour suppression d'un fournisseur
def supprimer_fournisseur(request, id_fournisseur):
    fournisseur = get_object_or_404(Fournisseurs, id_fournisseur=id_fournisseur)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    context = {'fournisseur': fournisseur}
    return render(request, 'supprimer_fournisseur.html', context)


# Tableau de bord utilisateur 

# Vue tableau de bord utilisateur

def tableau_de_bord_utilisateur(request):
    # votre code pour le tableau de bord ici
    return render(request, 'tableau_de_bord_utilisateur.html')
def deconnexion_utilisateur(request):
    logout(request)
    return redirect('login')

#Affectation


def affectation(request):
    if request.method == 'POST':
        form = AffectationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_affectations')
    else:
        form = AffectationForm()
    return render(request, 'affecter_equipement.html', {'form': form})
# liste affectaions
def liste_affectations(request):
    affectations = Affectations.objects.all()
    return render(request, 'liste_affectations.html', {'affectations': affectations})

# Modifier et supprimer  une affectation

def modifier_affectation(request, id_affectation):
    affectation = get_object_or_404(Affectations, pk=id_affectation)
    if request.method == 'POST':
        form = ModifierAffectationForm(request.POST, instance=affectation)
        if form.is_valid():
            form.save()
            return redirect('liste_affectations')
    else:
        form = ModifierAffectationForm(instance=affectation)
    return render(request, 'modifier_affectation.html', {'form': form})


def supprimer_affectation(request, id_affectation):
    affectation = get_object_or_404(Affectations, pk=id_affectation)
    if request.method == 'POST':
        affectation.delete()
        return redirect('liste_affectations')
    return render(request, 'supprimer_affectation.html', {'affectation': affectation})