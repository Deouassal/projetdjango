
  const form = document.querySelector('form');
  const emailInput = form.querySelector('#id_adresse_email');
  const passwordInput = form.querySelector('#id_mot_de_passe');

  function validateEmail() {
    const email = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      emailInput.setCustomValidity('Veuillez saisir une adresse email valide.');
    } else {
      emailInput.setCustomValidity('');
    }
  }

  function validatePassword() {
    const password = passwordInput.value.trim();
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(password)) {
      passwordInput.setCustomValidity('Le mot de passe doit contenir au moins 8 caractères, y compris des lettres majuscules et minuscules, des chiffres et des caractères spéciaux.');
    } else {
      passwordInput.setCustomValidity('');
    }
  }

  emailInput.addEventListener('input', validateEmail);
  passwordInput.addEventListener('input', validatePassword);

  form.addEventListener('submit', (event) => {
    // Valider les champs de formulaire avant la soumission
    validateEmail();
    validatePassword();
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    }
    form.classList.add('was-validated');
  });
