from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
def validate_description(value):
        if len(value) < 10:
            raise ValidationError('La description doit comporter au moins 10 caractères.')

# Table Utilisateurs
class Utilisateurs(models.Model):
    
    class Meta:
        db_table = "utilisateurs"

    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse_email = models.EmailField(max_length=254, unique=True)
    numero_telephone = models.CharField(max_length=20, validators=[MinLengthValidator(8, "Le numéro de téléphone doit avoir au moins %(limit_value)s chiffres.")])
    mot_de_passe = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            message="Le mot de passe doit contenir au moins 8 caractères, y compris des lettres majuscules et minuscules, des chiffres et des caractères spéciaux."
        )
    ])
    service = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    def str(self):
        return self.nom + ' ' + self.prenom


    def set_password(self, raw_password):
        self.mot_de_passe = make_password(raw_password)

# Table Fournisseurs
class Fournisseurs(models.Model):

    class Meta:
        db_table = "fournisseurs"
        constraints = [
            models.UniqueConstraint(fields=['adresse_email'], name='unique_adresse_email'),
            models.CheckConstraint(check=models.Q(site_web__regex=r'^https?://\S+$'), name='site_web_valide'),
        ]

    id_fournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    localisation = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    adresse_email = models.EmailField(max_length=255, unique=True)
    site_web = models.URLField(null=True)
    type_fournisseur = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adresse_email'], name='unique_adresse_email'),
            models.CheckConstraint(check=models.Q(site_web__regex=r'^https?://\S+$'), name='site_web_valide'),
        
        ]

    def clean(self):
        super().clean()
        if self.telephone:
            try:
                telephone_int = int(self.telephone)
            except ValueError:
                raise ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
            if telephone_int < 8:
                raise ValidationError("Le numéro de téléphone doit avoir au moins 8 chiffres.")

    def __str__(self):
        return self.nom



        
# Table Equipements
class Equipements(models.Model):

    class Meta:
        db_table = "Equipements"
        constraints = [
            models.CheckConstraint(check=models.Q(statut__in=['En stock', 'En service', 'Hors service']), name='statut_disponible'),
            models.UniqueConstraint(fields=['nom', 'numero_serie'], name='unique_equipement'),
        ]

    id_equipement = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    date_achat = models.DateField(null=True)
    date_debut_garantie = models.DateField(null=True)
    date_fin_garantie = models.DateField(null=True)
    statut = models.CharField(max_length=50)
    id_utilisateur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE, null=True)
    emplacement_actuel = models.CharField(max_length=50, null=True)
    id_fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.nom

# Table Consommables
class Consommables(models.Model):

    class Meta:
        db_table = "Consommables"
        constraints = [
            models.CheckConstraint(check=models.Q(quantite__gte=0), name='quantite_positive'),
        ]

    id_consommable = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    quantite = models.IntegerField()
    id_utilisateur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE, null=True)
    id_fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.nom

# Table MaterielsInformatiques
class Materiels_Informatiques(models.Model):

    class Meta:
        db_table = "materiels_informatiques"
        constraints = [
            models.CheckConstraint(check=models.Q(date_achat__lte=models.F('date_debut_garantie')), name='date_achat_inf_date_debut_garantie'),
            models.CheckConstraint(check=models.Q(date_debut_garantie__lte=models.F('date_fin_garantie')), name='date_debut_garantie_inf_date_fin_garantie'),
        ]

    id_materiel_informatique = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    numero_serie = models.CharField(max_length=50)
    date_achat = models.DateField(null=True)
    date_debut_garantie = models.DateField(null=True)
    date_fin_garantie = models.DateField(null=True)
    id_fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, null=True)
    id_utilisateur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE, null=True)

    def str(self):
        return f"{self.nom} ({self.numero_serie})"

# Table Administrateur

class administrateur(models.Model):

    class Meta:
        db_table = "administrateur"

    id_administrateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    USERNAME_FIELD = 'nom' #ou le nom du champ qui contient le nom d'utilisateur

    prénom = models.CharField(max_length=50)
    adresse_email = models.EmailField(max_length=254, unique=True)
    numero_telephone = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            message="Le mot de passe doit contenir au moins 8 caractères, y compris des lettres majuscules et minuscules, des chiffres et des caractères spéciaux."
        )
    ])
    autorisations = models.TextField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'adresse_email'


    def __str__(self):
        return f"{self.prénom} {self.nom}"

# Table Affectations


class Affectations(models.Model):
    class Meta:
        db_table = "Affectations"

    id_affectation = models.AutoField(primary_key=True)
    id_equipement = models.ForeignKey(Equipements, on_delete=models.CASCADE, null=True)
    id_consommable = models.ForeignKey(Consommables, on_delete=models.CASCADE, null=True)
    id_materiel_informatique = models.ForeignKey(Materiels_Informatiques, on_delete=models.CASCADE, null=True)
    id_utilisateur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE, null=True)
    date_affectation = models.DateField()
    date_retour = models.DateField(null=True)

    def __str__(self):
        if self.id_equipement:
            return f"Affectation de l'équipement {self.id_equipement} à l'utilisateur {self.id_utilisateur} le {self.date_affectation}"
        elif self.id_consommable:
            return f"Affectation du consommable {self.id_consommable} à l'utilisateur {self.id_utilisateur} le {self.date_affectation}"
        elif self.id_materiel_informatique:
            return f"Affectation du matériel informatique {self.id_materiel_informatique} à l'utilisateur {self.id_utilisateur} le {self.date_affectation}"

    # Contraintes de colonnes
    class Meta:
      constraints = [
        models.CheckConstraint(check=models.Q(date_retour__gte=models.F('date_affectation')), name='date_retour_posterieure_ou_egale'),
    ]


# Table Commande

class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.DateField()
    articles_commandes = models.CharField(max_length=50)
    quantite_commandee = models.IntegerField()
    statut_commande = models.CharField(max_length=50)
    id_fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, null=True)
    date_livraison_prevue = models.DateField()
    date_livraison_reelle = models.DateField(null=True)
    id_equipement = models.ForeignKey(Equipements, on_delete=models.CASCADE, null=True)
    id_consommable = models.ForeignKey(Consommables, on_delete=models.CASCADE, null=True)
    id_materiel_informatique = models.ForeignKey(Materiels_Informatiques, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "Commande"
        constraints = [
            models.CheckConstraint(check=models.Q(date_livraison_prevue__gte=models.F('date_commande')), name='date_livraison_prevue_posterieure_ou_egale'),
            models.CheckConstraint(check=models.Q(quantite_commandee__gt=0), name='quantite_commandee_positive'),
            models.CheckConstraint(check=models.Q(date_livraison_reelle__gte=models.F('date_livraison_prevue')), name='date_livraison_reelle_posterieure_ou_egale'),
            models.UniqueConstraint(fields=['id_equipement', 'id_consommable', 'id_materiel_informatique'], name='unique_article_commande'),
                 ]
        
    def __str__(self):
        return str(self.id_commande)




# Table Demandes

class Demandes(models.Model):
    class Meta:
        db_table = "Demandes"

        constraints = [
            models.CheckConstraint(check=models.Q(coût_reparation__gte=0), name='coût_reparation_positif'),
        ]

    id_demande = models.AutoField(primary_key=True)
    id_utilisateur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE, null=False)
    description_demande = models.TextField(validators=[validate_description])
    type_demande = models.CharField(max_length=50, choices=[('Maintenance', 'Maintenance'), ('Équipements', 'Équipements'), ('Consommables', 'Consommables'), ('Matérielsinformatiques', 'Matérielsinformatiques')])
    id_équipement = models.ForeignKey(Equipements, on_delete=models.CASCADE, null=True)
    id_consommable = models.ForeignKey(Consommables, on_delete=models.CASCADE, null=True)
    id_materiel_informatique = models.ForeignKey(Materiels_Informatiques, on_delete=models.CASCADE, null=True)
    date_demande = models.DateField(auto_now_add=True)
    état_demande = models.CharField(max_length=20, choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Terminée', 'Terminée')])
    coût_reparation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"{self.type_demande} - {self.date_demande}"
        

# Définition du signal pour définir l'état de la demande automatiquement
@receiver(post_save, sender=Demandes)
def definir_etat_demande(sender, instance, created, **kwargs):
    if created:
        if instance.type_demande == 'Maintenance':
            instance.état_demande = 'En attente'
        elif instance.type_demande in ['Équipements', 'Consommables', 'Matériels informatiques']:
            instance.état_demande = 'En cours'
        instance.save()



