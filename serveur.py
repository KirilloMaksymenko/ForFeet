from bottle import *
from bottle_sqlite import SQLitePlugin


install(SQLitePlugin("database/database.db"))


@route('<filename:path>')
def server_static(filename):
    """Redirige les liens utilisant les fichiers statiques
    vers le dossier /static"""
    return static_file(filename, root='static')


@route("/")
def index():
    """Capte tous les liens vers la route '/' et génère une page HTML
    à partir du template (modèle) index.tpl du dossier /view"""
    return template("index.tpl")


@route("/afficher")
def afficher(db):
    """Capte tous les liens vers la route '/afficher' et génère une page HTML
    à partir du template (modèle) afficher.tpl du dossier /view en utilisant
    la liste des résultats d'une requête SQL."""
    requete = db.execute('SELECT * FROM employe')  # exécution d'une requête SQL
    liste_employe = requete.fetchall()            # récupération des données liées à la requête
    return template("afficher.tpl", datas=liste_employe)

@post("/rechercher")
def rechercher(db):
    """Similaire à afficher() mais utilise le contenu d'un formulaire."""
    leNom = request.forms["NOM1"]        # récupération du contenu du champ NOM1
    lePrenom = request.forms["PRENOM1"]  # récupération du contenu du champ PRENOM1
    requete = db.execute('SELECT * FROM employe WHERE nom LIKE "{0}" OR prenom LIKE "{1}"'.format(leNom, lePrenom))
    liste_employe = requete.fetchall()
    if len(liste_employe) > 0:  # On teste si la requête a renvoyé des élèves ou pas
        return template("afficher.tpl", datas=liste_employe)
    else:
        return template("erreur.tpl")


@post("/ajouter")
def ajouter(db):
    """Capte tous les liens vers la route '/ajouter', exécute une requête à
    partir d'un formulaire et génère une page HTML à partir du template (modèle)
    confirmation.tpl du dossier /view."""
    leNom = request.forms["NOM2"]
    lePrenom = request.forms["PRENOM2"]
    db.execute('INSERT INTO employe VALUES ("{0}", "{1}")'.format(leNom, lePrenom))
    return template("confirmation.tpl", nom=leNom, prenom=lePrenom)


@post("/supprimer")
def supprimer(db):
    """Capte tous les liens vers la route '/supprimer', exécute une requête à
    partir d'un formulaire et génère une page HTML à partir du template (modèle)
    <A compléter>.tpl du dossier /view."""
    pass


if __name__ == "__main__":
    # Modifier le numéro de port selon les indications du professeur
    run(reloader=True,
        debug=True,
        host="127.0.0.1",
        port=7077)
