from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm , ConnexionForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from projetstage.models import administrateur
from .forms import AjouterEquipementForm
from .models import Fournisseurs
from .forms import FournisseurForm
from .models import Utilisateurs
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import forms
from .forms import InscriptionAdminForm, ConsommablesForm, SupprimerConsommableForm, DemandeForm, SupprimerDemandeForm, LoginForm
#from django.contrib.auth.decorators import login_required
from .models import Consommables, Commande, Affectations, Demandes
from .models import Equipements , Materiels_Informatiques
from .forms import AffectationForm, DemandeForm, AjouterConsommableForm,AjouterMaterielForm, EquipementForm, SupprimerMaterielInformatiqueForm, MaterielsInformatiquesForm
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.views import LoginView




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

def connexion_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'connexion_admin.html', context)

def index_admin(request):
    return render(request, 'admin_index.html')

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
        nom = request.POST['nom']
        description = request.POST['description']
        quantite = request.POST['quantite']
        id_utilisateur = request.POST.get('id_utilisateur')
        
        if id_utilisateur and id_utilisateur.strip().isdigit():
            utilisateur = Utilisateurs.objects.get(pk=int(id_utilisateur))
        else:
            utilisateur = None
        
        id_fournisseur = request.POST.get('id_fournisseur')
        
        if id_fournisseur and id_fournisseur.strip().isdigit():
            fournisseur = Fournisseurs.objects.get(pk=int(id_fournisseur))
        else:
            fournisseur = None
        
        consommable = Consommables(
            nom=nom,
            description=description,
            quantite=quantite,
            id_utilisateur=utilisateur,
            id_fournisseur=fournisseur,
        )
        consommable.save()
        return redirect('liste_consommables')
    else:
        return render(request, 'ajouter_consommable.html')


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

def ajouter_equipement(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        numero_serie = request.POST['numero_serie']
        date_achat = request.POST['date_achat']
        date_debut_garantie = request.POST['date_debut_garantie']
        date_fin_garantie = request.POST['date_fin_garantie']
        statut = request.POST['statut']
        id_utilisateur = request.POST.get('id_utilisateur')
        utilisateur = Utilisateurs.objects.get(pk=id_utilisateur)
        emplacement_actuel = request.POST['emplacement_actuel']
        id_fournisseur = request.POST.get('id_fournisseur')
        fournisseur = Fournisseurs.objects.get(pk=id_fournisseur)
        equipement = Equipements(
            nom=nom,
            numero_serie=numero_serie,
            date_achat=date_achat,
            date_debut_garantie=date_debut_garantie,
            date_fin_garantie=date_fin_garantie,
            statut=statut,
            id_utilisateur=utilisateur,
            emplacement_actuel=emplacement_actuel,
            id_fournisseur=fournisseur,
        )
        equipement.statut = 'En stock' # ou 'En service' ou 'Hors service'
        equipement.save()
        return redirect('liste_equipements')
    else:
        
        return render(request, 'ajouter_equipement.html')


def ajouter_materiel(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        description = request.POST['description']
        numero_serie = request.POST['numero_serie']
        date_achat = request.POST['date_achat']
        date_debut_garantie = request.POST['date_debut_garantie']
        date_fin_garantie = request.POST['date_fin_garantie']
        id_utilisateur = request.POST.get('id_utilisateur')
        
        if id_utilisateur and id_utilisateur.strip().isdigit():
            utilisateur = Utilisateurs.objects.get(pk=int(id_utilisateur))
        else:
            utilisateur = None
        
        id_fournisseur = request.POST.get('id_fournisseur')
        
        if id_fournisseur and id_fournisseur.strip().isdigit():
            fournisseur = Fournisseurs.objects.get(pk=int(id_fournisseur))
        else:
            fournisseur = None
        
        materiel = Materiels_Informatiques(
            nom=nom,
            description=description,
            numero_serie=numero_serie,
            date_achat=date_achat,
            date_debut_garantie=date_debut_garantie,
            date_fin_garantie=date_fin_garantie,
            id_utilisateur=utilisateur,
            id_fournisseur=fournisseur,
        )
        materiel.save()
        return redirect('liste_materiel_informatique')
    else:
        return render(request, 'ajouter_materiel_informatique.html')

#Affectation


def affecter_equipement(request, demande_id):
    demande = Demandes.objects.get(pk=demande_id)
    if request.method == 'POST':
        form = AffectationForm(request.POST)
        if form.is_valid():
            affectation = form.save(commit=False)
            affectation.id_equipement = demande.id_équipement
            affectation.id_consommable = demande.id_consommable
            affectation.id_materiel_informatique = demande.id_materiel_informatique
            affectation.id_utilisateur = demande.id_utilisateur
            affectation.save()
            demande.delete()
            if affectation.date_retour:
                return redirect('update_affectation', affectation_id=affectation.id)
            else:
                return redirect('liste_affectations')
    else:
        form = AffectationForm()
    return render(request, 'affecter_equipement.html', {'form': form, 'demande': demande})

# Enregister commande 
def enregistrer_commande(request):
    if request.method == 'POST':
        date_commande = request.POST['date_commande']
        articles_commandes = request.POST.get('articles_commandes')
        quantite_commandee = request.POST.get('quantite_commandee')
        statut_commande = request.POST.get('statut_commande')
        id_fournisseur = request.POST.get('id_fournisseur')
        date_livraison_prevue = request.POST['date_livraison_prevue']
        id_equipement = request.POST.get('id_equipement')
        id_consommable = request.POST.get('id_consommable')
        id_materiel_informatique = request.POST.get('id_materiel_informatique')

        commande = Commande(
            date_commande=date_commande,
            articles_commandes=articles_commandes,
            quantite_commandee=quantite_commandee,
            statut_commande=statut_commande,
            id_fournisseur_id=id_fournisseur,
            date_livraison_prevue=date_livraison_prevue,
            id_equipement_id=id_equipement,
            id_consommable_id=id_consommable,
            id_materiel_informatique_id=id_materiel_informatique
        )
        commande.save()

        return redirect('liste_commandes')
    else:
        fournisseurs = Fournisseurs.objects.all()
        equipements = Equipements.objects.all()
        consommables = Consommables.objects.all()
        materiels_informatiques = Materiels_Informatiques.objects.all()
        return render(request, 'enregistrer_commande.html', {'fournisseurs': fournisseurs, 'equipements': equipements, 'consommables': consommables, 'materiels_informatiques': materiels_informatiques})
#vue liste commande 
def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'liste_commandes.html', {'commandes': commandes})
def affectations(request):
    affectations = Affectations.objects.all()
    return render(request, 'liste_affectations.html', {'affectations': affectations})
 
def demander_equipement(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_demandes')
    else:
        form = DemandeForm()
    return render(request, 'demander_equipement.html', {'form': form})

def liste_demandes(request):
    demandes = Demandes.objects.all()
    return render(request, 'liste_demandes.html', {'demandes': demandes})


def update_affectation(request, affectation_id):
    affectation = Affectation.objects.get(pk=affectation_id)
    if request.method == 'POST':
        form = AffectationUpdateForm(request.POST, instance=affectation)
        if form.is_valid():
            form.save()
            return redirect('liste_affectations')
    else:
        form = AffectationUpdateForm(instance=affectation)
    return render(request, 'update_affectation.html', {'form': form})


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
        form = DemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('liste_demandes')
    else:
        form = DemandeForm(instance=demande)
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


def vue_connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger vers la page de destination après la connexion réussie
            return redirect('demandes')
        else:
            # Afficher un message d'erreur si la connexion a échoué
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'connexion.html')

def vue_deconnexion(request):
    logout(request)
    return redirect('connexion')

#
#class vueLoginView(LoginView):
    #template_name = 'login.html'
    #fields = {'adresse_email': 'email', 'mot_de_passe': 'password'}


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            adresse_email = form.cleaned_data['adresse_email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            user = authenticate(request, username=adresse_email, password=mot_de_passe)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "L'adresse e-mail ou le mot de passe est incorrect.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        adresse_email = request.POST.get('adresse_email')
        mot_de_passe = request.POST.get('mot_de_passe')
        user = authenticate(request, adresse_email=adresse_email, password=mot_de_passe)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Adresse email ou mot de passe incorrect.')
    return render(request, 'login.html')