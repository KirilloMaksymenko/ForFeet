# SOMMAIRE

[[_TOC_]]

# ABSTRACT

Ce projet permet de créer un serveur web en utilisant Python et la bibliothèque `Bottle`. Une base de donnée SQL est également expoitée grâce à `Bottle_SQlite` afin de réaliser un site web dynamique. 

# ARBORESCENCE

- `/` : racine du projet, contient uniquement le fichier `serveur.py`
- `/database` : contient le (ou les) fichier(s) de base de donnée
- `/static` : contient les fichiers statiques : CSS, images, script JS
- `/views` : contient les templates (fichiers `.tpl` servant de modèle à la génération des fichiers `.html`)

# TECHNOLOGIES

- Python 3.X
    - `Bottle`
    - `Bottle_SQLite`
- HTML
- CSS
- JS
- SQL

# HOW TO

## Faire un FORK du projet

Pour commencer ce projet, cliquer sur le bouton `Créer une bifurcation` en haut à droite de la page de dépôt. 

## Importer le projet en local

Ouvrez votre propre projet et cliquez sur le bouton `Code`. Enfin, copiez l'adresse indiquée dans `Cloner avec HTTPS`. 

Ouvrez `Pycharm` et importez le projet sur votre disque grâce à `Get from VCS`. 

## Lire les fichiers TPL

Ouvrez un fichier `.tpl` du dossier `views` avec `Pycharm`. Le logiciel devrait vous indiquer dans un bandeau qu'il ne peut pas lire ce type de fichier. À l'aide du bandeau, paramétrez le logiciel en indiquant `*.tpl` dans les extensions possibles du HTML. 

Si aucun bandeau ne s'affiche, ouvrez les propriétés de `Pycharm` puis sélectionnez `Editor > File types`. 

## Choix du numéro de port

Pour faciliter la correction à la dernière ligne du fichier `serveur.py`, modifier le paramètre `port=7000` par votre numéro perso de la manière suivante :

- prenez l'initiale en majusucule de votre prénom (_Exemple : `A` pour Alphonse_)
- prenez son code ASCII (_Exemple : `ord("A")` renvoie 65 pour Alphonse_)
- additionnez 7000 et vous aurez votre numéro de port perso (_Exemple : `65+7000=7065` pour Alphonse_)

##  Visualisation du site

Exécutez `serveur.py` puis, au choix : 

- `Pycharm` affiche une adresse du type `http://127.0.0.1:7065/`. Cliquez dessus pour l'ouvrir dans votre navigateur. 
- Ouvrez un navigateur et entrez l'adresse suivante `localhost:7065/` (en remplaçant `7065` par votre numéro de port perso). 