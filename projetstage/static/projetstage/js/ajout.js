// Récupérer le formulaire et les champs
const form = document.querySelector('form');
const nom = document.getElementById('nom');
const numero_serie = document.getElementById('numero_serie');
const date_achat = document.getElementById('date_achat');
const date_debut_garantie = document.getElementById('date_debut_garantie');
const date_fin_garantie = document.getElementById('date_fin_garantie');
const statut = document.getElementById('statut');
const id_utilisateur = document.getElementById('id_utilisateur');
const emplacement_actuel = document.getElementById('emplacement_actuel');
const id_fournisseur = document.getElementById('id_fournisseur');

// Ajouter un écouteur d'événement sur le formulaire pour intercepter la soumission
form.addEventListener('submit', function(event) {
  // Vérifier que les champs sont valides
  if (!nom.value.trim() || !numero_serie.value.trim() || !date_achat.value.trim() || !date_debut_garantie.value.trim() || !date_fin_garantie.value.trim() || !statut.value.trim() || !id_utilisateur.value.trim() || !emplacement_actuel.value.trim() || !id_fournisseur.value.trim()) {
    // Si un champ est invalide, empêcher l'envoi du formulaire et afficher un message d'erreur
    event.preventDefault();
    alert('Veuillez remplir tous les champs.');
  }
});





// Ciblez tous les formulaires de suppression d'équipement avec la classe "supprimer-equipement-form"
const supprimerEquipementForms = document.querySelectorAll('.supprimer-equipement-form');

// Parcourez tous les formulaires de suppression d'équipement
supprimerEquipementForms.forEach(form => {
  // Ajoutez un événement "submit" à chaque formulaire
  form.addEventListener('submit', (event) => {
    // Empêchez le formulaire de se soumettre automatiquement
    event.preventDefault();
    // Demandez à l'utilisateur de confirmer la suppression
    const confirmSuppression = window.confirm('Voulez-vous vraiment supprimer cet équipement ?');
    // Si l'utilisateur a confirmé la suppression, soumettez le formulaire
    if (confirmSuppression) {
      form.submit();
    }
  });
});


//

const selectEquipement = document.getElementById('id_nom');
  selectEquipement.addEventListener('change', (event) => {
    const equipementId = event.target.value;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/equipements/${equipementId}/details/`);
    xhr.onload = () => {
      if (xhr.status === 200) {
        const equipement = JSON.parse(xhr.responseText);
        const form = document.getElementById('formulaire-modification');
        form.elements.numero_serie.value = equipement.numero_serie;
        form.elements.date_achat.value = equipement.date_achat;
        form.elements.date_debut_garantie.value = equipement.date_debut_garantie;
        form.elements.date_fin_garantie.value = equipement.date_fin_garantie;
        form.elements.statut.value = equipement.statut;
        form.elements.id_utilisateur.value = equipement.id_utilisateur;
        form.elements.emplacement_actuel.value = equipement.emplacement_actuel;
        form.elements.id_fournisseur.value = equipement.id_fournisseur;
      } else {
        alert('Une erreur est survenue lors de la récupération des données d\'équipement.');
      }
    };
    xhr.send();
  });

