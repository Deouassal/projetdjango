// Sélectionnez les éléments HTML pertinents
var selectDemande = document.getElementById('id_type_demande');
var champEquipement = document.getElementById('id_equipement');
var champMaterielInformatique = document.getElementById('id_materiel_informatique');
var champConsommable = document.getElementById('id_consommable');

// Ajoutez un écouteur d'événement pour le changement de sélection de demande
selectDemande.addEventListener('change', function(event) {
  var typeDemande = event.target.value;
  // Rendre le champ Equipement obligatoire si le type de demande est "Equipement"
  if (typeDemande === 'Equipement') {
    champEquipement.required = true;
    champMaterielInformatique.required = false;
    champConsommable.required = false;
  }
  // Rendre le champ Matériel informatique obligatoire si le type de demande est "Matériel informatique"
  else if (typeDemande === 'Matériel informatique') {
    champEquipement.required = false;
    champMaterielInformatique.required = true;
    champConsommable.required = false;
  }
  // Rendre le champ Consommable obligatoire si le type de demande est "Consommable"
  else if (typeDemande === 'Consommable') {
    champEquipement.required = false;
    champMaterielInformatique.required = false;
    champConsommable.required = true;
  }
  // Rendre tous les champs facultatifs si aucun type de demande n'est sélectionné
  else {
    champEquipement.required = false;
    champMaterielInformatique.required = false;
    champConsommable.required = false;
  }
});