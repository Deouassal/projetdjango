// Fonction pour envoyer une requête AJAX pour ajouter un fournisseur
function ajouterFournisseur() {
    // Récupérer les données du formulaire de fournisseur
    const formFournisseur = document.querySelector('#form-fournisseur');
    const formData = new FormData(formFournisseur);

    // Envoyer une requête POST AJAX pour ajouter le fournisseur
    const url = formFournisseur.action;
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch(url, {
        method: formFournisseur.method,
        body: formData,
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        if (response.ok) {
            // Recharger la page pour afficher le fournisseur ajouté
            window.location.reload();
        } else {
            // Afficher une erreur si la requête a échoué
            console.error('Erreur lors de la soumission du formulaire de fournisseur');
        }
    });
}

// Gestionnaire d'événement pour le formulaire de fournisseur
document.addEventListener('DOMContentLoaded', () => {
    const formFournisseur = document.querySelector('#form-fournisseur');
    if (formFournisseur) {
        // Ajouter un gestionnaire d'événement pour le bouton "Enregistrer" du formulaire de fournisseur
        const btnEnregistrer = formFournisseur.querySelector('#btn-enregistrer');
        btnEnregistrer.addEventListener('click', (event) => {
            event.preventDefault();
            // Valider le formulaire de fournisseur avant de l'envoyer
            const fournisseurForm = new FournisseurForm(formFournisseur);
            if (fournisseurForm.validate()) {
                // Envoyer la requête AJAX pour ajouter le fournisseur
                ajouterFournisseur();
            }
        });

        // Ajouter un gestionnaire d'événement pour le bouton "Annuler" du formulaire de fournisseur
        const btnAnnuler = formFournisseur.querySelector('#btn-annuler');
        btnAnnuler.addEventListener('click', (event) => {
            event.preventDefault();
            // Recharger la page pour annuler l'ajout du fournisseur
            window.location.reload();
        });
    }
});