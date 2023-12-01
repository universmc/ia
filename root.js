const express = require('express');
const app = express();

// Définir le répertoire 'public' comme répertoire de fichiers statiques
app.use(express.static('public'));

// Démarrer le serveur
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur le port ${PORT}`);
});
