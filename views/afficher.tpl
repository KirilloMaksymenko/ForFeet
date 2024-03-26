<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8"/>
    <link rel="stylesheet" href="style.css"/>
    <link rel="icon" href="favicon.png"/>
    <title>Profnote 0.1</title>
</head>
<body>
    <!--Entête-->
    <header>
        <h1>Profnote</h1>
    </header>

    <!--Barre de navigation-->
    <nav>
        <div class="liens">
            <a href="/">🏠 Accueil</a>
        </div>
        <div class="liens">
            <a href="afficher">Afficher la base</a>
        </div>
    </nav>

    <!--Corps de page-->
    <section>
        <h2>Les élèves recherchés</h2>
        <table>
            <tr>
                <th>NOM</th>
                <th>Prénom</th>
            </tr>
            %for eleve in datas:
            <tr>
                <td>{{eleve[0]}}</td>
                <td>{{eleve[1]}}</td>
            </tr>
            %end
        </table>
    </section>

    <!--Pied de page-->
    <div id="footer">
        Site réalisé par Vincent JARC.
    </div>
</body>
</html>