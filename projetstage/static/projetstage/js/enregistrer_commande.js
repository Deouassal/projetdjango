// Récupération des éléments du formulaire
const form = document.querySelector('form');
const dateCommandeInput = document.getElementById('date_commande');
const articlesCommandesInput = document.getElementById('articles_commandes');
const quantiteCommandeeInput = document.getElementById('quantite_commandee');
const statutCommandeInput = document.getElementById('statut_commande');
const idFournisseurInput = document.getElementById('id_fournisseur');
const dateLivraisonPrevueInput = document.getElementById('date_livraison_prevue');
const idEquipementInput = document.getElementById('id_equipement');
const idConsommableInput = document.getElementById('id_consommable');
const idMaterielInformatiqueInput = document.getElementById('id_materiel_informatique');

// Fonction de validation du formulaire
function validateForm() {
  let valid = true;

  // Validation du champ date de commande
  if (dateCommandeInput.value === '') {
    dateCommandeInput.classList.add('is-invalid');
    valid = false;
  } else {
    dateCommandeInput.classList.remove('is-invalid');
  }

  // Validation du champ articles commandés
  if (articlesCommandesInput.value === '') {
    articlesCommandesInput.classList.add('is-invalid');
    valid = false;
  } else {
    articlesCommandesInput.classList.remove('is-invalid');
  }

  // Validation du champ quantité commandée
  if (quantiteCommandeeInput.value === '' || quantiteCommandeeInput.value <= 0) {
    quantiteCommandeeInput.classList.add('is-invalid');
    valid = false;
  } else {
    quantiteCommandeeInput.classList.remove('is-invalid');
  }

  // Validation du champ statut de la commande
  if (statutCommandeInput.value === '') {
    statutCommandeInput.classList.add('is-invalid');
    valid = false;
  } else {
    statutCommandeInput.classList.remove('is-invalid');
  }

  // Validation du champ fournisseur
  if (idFournisseurInput.value === '') {
    idFournisseurInput.classList.add('is-invalid');
    valid = false;
  } else {
    idFournisseurInput.classList.remove('is-invalid');
  }

  // Validation du champ date de livraison prévue
  if (dateLivraisonPrevueInput.value === '') {
    dateLivraisonPrevueInput.classList.add('is-invalid');
    valid = false;
  } else {
    dateLivraisonPrevueInput.classList.remove('is-invalid');
  }

  // Validation du champ équipement, consommable ou matériel informatique
  if (idEquipementInput.value === '' && idConsommableInput.value === '' && idMaterielInformatiqueInput.value === '') {
    idEquipementInput.classList.add('is-invalid');
    idConsommableInput.classList.add('is-invalid');
    idMaterielInformatiqueInput.classList.add('is-invalid');
    valid = false;
  } else {
    idEquipementInput.classList.remove('is-invalid');
    idConsommableInput.classList.remove('is-invalid');
    idMaterielInformatiqueInput.classList.remove('is-invalid');
  }

  return valid;
}

// Gestionnaire d'événement pour la soumission du formulaire
form.addEventListener('submit', (event) => {
  if (!validateForm()) {
    event.preventDefault();
  }
});