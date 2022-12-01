# fancy-fencing
## Description
Ce jeu est un projet réalisé dans le cadre du module "Programmation Avancée" en Master 1 RSA (Réseaux et Systèmes Autonomes).

Il représente un match d'escrime jouable par deux personnes localement.

## Lancement du jeu
```bash
python3 main.py fps [save_file]
```

`fps` correspond au nombre d'images par secondes affichées par le jeu
`save_file` est optionnel et correspond au fichier à charger pour reprendre une partie préalablement sauvegardée.

## Scène
Lorsque le programme se lance, celui-ci va chercher à récupérer un format de scène dans un fichier d'extension `.ffscene` (par défaut (`default.ffscene`). Ce format est ensuite testé afin de déterminer si celui-ci est conforme puis est utilisé pour créer une instance de classe `Scene` contenant les positions des joueurs, des obstacles et la longueur.

## Contrôles
| Touches                | Action                                        |
| ---------------------- | --------------------------------------------- |
| Q/D                    | Déplacement du joueur 1 vers la gauche/droite |
| A/E                    | Saut du joueur 1 vers la gauche/droite        |
| Z                      | Passage en mode "attaque" du joueur 1         |
| S                      | Passage en mode "défense" du joueur           |
| LEFT_ARROW/RIGHT_ARROW | Déplacement du joueur 2 vers la gauche/droite |
| L/M                    | Saut du joueur 2 vers la gauche/droite        |
| O                      | Passage en mode "attaque" du joueur 2         |
| P                      | Passage en mode "défense" du joueur 2         |
| B                      | Affichage du menu "Pause"                     |
| G                      | Arrêt du jeu (en pause uniquement)            |
| J                      | Sauvegarde de la partie (en pause uniquement) |

Les joueurs possèdent les caractéristiques suivantes:
- `movement_speed`: délai après lequel chaque mouvement sera effectif
- `attacking_range`: portée de l'épée du joueur
- `defending_range`: portée du bouclier pour contrer une attaque
- `blocking_time`: délai pendant lequel un joueur peut rester en mode "défense"
Ces caractéristiques sont modifiables dans un fichier propre à chaque joueur (`p1.ffplayer` ou `p2.ffplayer`) ou dans les fichiers de sauvegarde créés.

## Sauvegarde de la partie
Lorsque la partie est en pause, il est possible de la sauvegarder comme mentionné plus tôt, cette sauvegarde reprend la forme de la scène, les caractéristiques des joueurs, leurs positions respectives ainsi que le score. Toutes ces données sont stockées dans un fichier de format `save_%J%-%M%-%A%_%h%-%m%-%s%`.ffsave qu'il est possible d'appeler en paramètre de lancement du programme afin de reprendre la partie.
