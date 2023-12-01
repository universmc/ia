// templates/script.js
acts.forEach((act, index) => {
    setTimeout(() => {
      console.log(act.text);
      // Ajoutez ici le code spécifique à chaque acte, si nécessaire.
    }, act.duration);
  });
  