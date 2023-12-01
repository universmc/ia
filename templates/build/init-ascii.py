def afficher_script_dashboard(titre, status):
    # Caractères ASCII
    topLeft = '╔'
    horizontal = '═'
    topRight = '╗'
    vertical = '║'
    bottomLeft = '╚'
    bottomRight = '╝'

def afficher_script_dashboard(titre, status):
    # Caractères ASCII
    upperHalfBlock = '▀'
    lowerHalfBlock = '▄'
    fullBlock = '█'
    leftHalfBlock = '▌'
    rightHalfBlock = '▐'
    lightShade = '░'
    mediumShade = '▒'
    darkShade = '▓'

    # Longueur de la ligne horizontale
    longueur_ligne = max(len(f" Titre du Script : {titre} "), len(f" Status du Script : {status} "))

    # Espacement entre le texte et les bordures
    espacement = 2

    # Longueur de la ligne horizontale
    longueur_ligne = max(len(f" Titre du Script : {titre} "), len(f" Status du Script : {status} "))

    # Affichage du tableau de bord
    print(leftHalfBlock + upperHalfBlock * (longueur_ligne + espacement) + rightHalfBlock)
    print(lightShade + f" Titre du Script : {titre:<{longueur_ligne}} " + lightShade)
    print(mediumShade + fullBlock * (longueur_ligne + espacement) + mediumShade)
    print(lightShade + f" Status du Script : {status:<{longueur_ligne}} " + lightShade)
    print(leftHalfBlock + lowerHalfBlock * (longueur_ligne + espacement) + rightHalfBlock)

# Exemple d'utilisation
afficher_script_dashboard("Script Pilote 1", "En attente")
