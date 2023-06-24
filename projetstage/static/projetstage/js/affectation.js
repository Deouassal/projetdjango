const affectationForm = document.getElementById('affectationForm');
  affectationForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const dateAffectation = document.getElementById('date_affectation').value;
    const dateRetour = document.getElementById('date_retour').value || null;
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onload = () => {
      if (xhr.status === 200) {
        window.location.href = '/liste-affectations/';
      } else {
        alert('Une erreur est survenue lors de l\'enregistrement de l\'affectation.');
      }
    };
    xhr.send(`date_affectation=${dateAffectation}&date_retour=${dateRetour}&csrfmiddlewaretoken=${csrfToken}`);
  });