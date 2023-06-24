from django import forms
from projetstage.models import Utilisateurs
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from projetstage.models import administrateur
from django.contrib.auth.forms import UserCreationForm
import re
from .models import Equipements, Materiels_Informatiques
from .models import Fournisseurs, Demandes 
from .models import Materiels_Informatiques
from .models import Consommables, Affectations
from django.contrib.auth.hashers import check_password






class SignUpForm(forms.ModelForm):
    mot_de_passe = forms.CharField(label='Mot de passe', widget=forms.PasswordInput, validators=[
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            message="Le mot de passe doit contenir au moins 8 caractères, y compris des lettres majuscules et minuscules, des chiffres et des caractères spéciaux."
        )
    ])
    numero_telephone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'})
    )

    def clean_numero_telephone(self):
        numero_telephone = self.cleaned_data.get('numero_telephone')
        if len(numero_telephone) < 8:
            raise forms.ValidationError("Le numéro de téléphone doit avoir au moins 8 chiffres.")
        return numero_telephone
    class Meta:
        model = Utilisateurs
        fields = ('nom', 'prenom', 'adresse_email', 'numero_telephone', 'service', 'poste', 'mot_de_passe')
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse_email': 'Adresse email',
            'numero_telephone': 'Numéro de téléphone',
            'service': 'Service',
            'poste': 'Poste',
            'mot_de_passe': 'Mot de passe',
        }
        help_texts = {
             'nom': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'})),
             'prenom': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre prénom'})),
             'adresse_email': forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse email'})),
             'numero_telephone': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'})),
             'service': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre service'})),
             'poste': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre poste'}))
        }
            
        error_messages = {
            'adresse_email': {
                'unique': "Un utilisateur avec cette adresse email existe déjà."
            }
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["mot_de_passe"])
        if commit:
            user.save()
        return user

class ConnexionForm(forms.Form):
    adresse_email = forms.EmailField(
        max_length=254,
        label='Adresse e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre adresse email'
            }
        )
    )
    mot_de_passe = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        label='Mot de passe',
        validators=[
            RegexValidator(
                regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Le mot de passe doit contenir au moins 8 caractères, y compris des lettres majuscules et minuscules, des chiffres et des caractères spéciaux."
            )
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        adresse_email = cleaned_data.get('adresse_email')
        mot_de_passe = cleaned_data.get('mot_de_passe')
        if adresse_email and mot_de_passe:
            try:
                utilisateur = Utilisateurs.objects.get(adresse_email=adresse_email)
                if not check_password(mot_de_passe, utilisateur.mot_de_passe):
                    raise forms.ValidationError("Nom d'utilisateur ou mot de passe incorrect.")
            except Utilisateurs.DoesNotExist:
                raise forms.ValidationError("Nom d'utilisateur ou mot de passe incorrect.")
        return cleaned_data
#page admin 

class InscriptionAdminForm(UserCreationForm):
    nom = forms.CharField(max_length=50, required=True)
    prénom = forms.CharField(max_length=50, required=True)
    adresse_email = forms.EmailField(max_length=254, required=True)
    numero_telephone = forms.CharField(max_length=20, required=True)
    autorisations = forms.CharField(max_length=50, required=True)

    class Meta:
        model = administrateur
        fields = ['nom', 'prénom', 'adresse_email', 'numero_telephone', 'mot_de_passe', 'autorisations']

    def __init__(self, *args, **kwargs):
        super(InscriptionAdminForm, self).__init__(*args, **kwargs)
        self.fields['mot_de_passe'].label = 'Mot de Passe'

    def clean_adresse_email(self):
        adresse_email = self.cleaned_data['adresse_email']
        if administrateur.objects.filter(adresse_email=adresse_email).exists():
            raise ValidationError("Un administrateur avec cette adresse e-mail existe déjà.")
        return adresse_email


    def clean_numero_telephone(self):
        numero_telephone = self.cleaned_data.get('numero_telephone')
        if not isinstance(numero_telephone, str):
            raise forms.ValidationError("Le numéro de téléphone doit être une chaîne de caractères.")
        elif len(numero_telephone) < 8:
            raise forms.ValidationError("Le numéro de téléphone doit avoir au moins 8 chiffres.")
        else:
            try:
                int(numero_telephone)
            except ValueError:
                raise forms.ValidationError("Le numéro de téléphone doit être un entier.")
        return numero_telephone

class ConnexionAdminForm(forms.Form):
    adresse_email = forms.EmailField(max_length=254, required=True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        adresse_email = cleaned_data.get("adresse_email")
        mot_de_passe = cleaned_data.get("mot_de_passe")
        if adresse_email and mot_de_passe:
            administrateur = authenticate(request=None, username=adresse_email, password=mot_de_passe)
            
            if not administrateur:
                raise ValidationError("L'adresse e-mail ou le mot de passe est incorrect.")
            elif not admin.check_password(mot_de_passe):
                raise ValidationError("L'adresse e-mail ou le mot de passe est incorrect.")

        return cleaned_data


class AjouterEquipementForm(forms.ModelForm):
    
    CHOICES = [
        ('En stock', 'En stock'),
        ('En service', 'En service'),
        ('Hors service', 'Hors service'),
    ]

    statut = forms.ChoiceField(choices=CHOICES)
    
    
    class Meta:
        model = Equipements
        fields = ['nom', 'numero_serie', 'date_achat', 'date_debut_garantie', 'date_fin_garantie', 'statut', 'id_utilisateur', 'emplacement_actuel', 'id_fournisseur']

        
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs
        fields = ['nom', 'prenom', 'localisation', 'telephone', 'adresse_email', 'site_web', 'type_fournisseur', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if telephone:
            try:
                telephone_int = int(telephone)
            except ValueError:
                raise forms.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
            if telephone_int < 8:
                raise forms.ValidationError("Le numéro de téléphone doit avoir au moins 8 chiffres.")
        return telephone


class AjouterMaterielInformatiqueForm(forms.ModelForm):

    class Meta:
        model = Materiels_Informatiques
        fields = ['nom', 'numero_serie', 'date_achat', 'date_debut_garantie', 'date_fin_garantie', 'id_utilisateur', 'id_fournisseur']

class AjouterConsommableForm(forms.ModelForm):
    class Meta:
        model = Consommables
        fields = ['nom', 'description', 'quantite', 'id_utilisateur', 'id_fournisseur']

class AffectationForm(forms.ModelForm):
    date_affectation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_retour = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Affectations
        fields = ['id_equipement', 'id_consommable', 'id_materiel_informatique', 'id_utilisateur', 'date_affectation', 'date_retour']
        labels = {
            'id_equipement': 'Équipement',
            'id_consommable': 'Consommable',
            'id_materiel_informatique': 'Matériel informatique',
            'id_utilisateur': 'Utilisateur',
        }       

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demandes
        fields = ['id_utilisateur', 'description_demande', 'type_demande', 'id_équipement', 'id_consommable', 'id_materiel_informatique', 'coût_reparation']

class AjouterMaterielForm(forms.ModelForm):
    class Meta:
        model = Materiels_Informatiques
        fields = ['nom', 'description', 'numero_serie', 'date_achat', 'date_debut_garantie', 'date_fin_garantie', 'id_utilisateur', 'id_fournisseur']


# Mise à jour de la table affectation

class AffectationUpdateForm(forms.ModelForm):
    class Meta:
        model = Affectations
        fields = ['date_retour']

    date_retour = forms.DateField(required=False, label='Date de retour')

# formulaire de modification et de suppression d'un équipement 

class EquipementForm(forms.ModelForm):
    
    class Meta:
        model = Equipements
        fields = ['nom', 'numero_serie', 'date_achat', 'date_debut_garantie', 'date_fin_garantie', 'statut', 'id_utilisateur', 'emplacement_actuel', 'id_fournisseur']

class SupprimerEquipementForm(forms.Form):
    confirm = forms.BooleanField(label='Confirmer la suppression', required=True)

# formulaire de modification et de suppression d'un matériel informatique

class MaterielsInformatiquesForm(forms.ModelForm):
    class Meta:
        model = Materiels_Informatiques
        fields = ['nom', 'description', 'numero_serie', 'date_achat', 'date_debut_garantie', 'date_fin_garantie', 'id_fournisseur', 'id_utilisateur']

class SupprimerMaterielInformatiqueForm(forms.Form):
    confirm = forms.BooleanField(label='Confirmer la suppression', required=True)


# formulaire de modification et de suppression d'un consommable 

class ConsommablesForm(forms.ModelForm):
    class Meta:
        model = Consommables
        fields = ['nom', 'description', 'quantite', 'id_fournisseur', 'id_utilisateur']


class SupprimerConsommableForm(forms.Form):
    confirm = forms.BooleanField(label='Confirmer la suppression', required=True)
#
class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demandes
        fields = ['type_demande', 'description_demande', 'id_utilisateur', 'id_équipement', 'id_consommable', 'id_materiel_informatique', 'état_demande', 'coût_reparation']


class SupprimerDemandeForm(forms.Form):
    confirm = forms.BooleanField(label='Confirmer la suppression', required=True)

class LoginForm(forms.Form):
    adresse_email = forms.EmailField(label='Adresse e-mail', max_length=254)
    mot_de_passe = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)