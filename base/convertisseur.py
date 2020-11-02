from markdown import markdown
import os, sys

def convert_and_create_static_site():
    # ouverture du fichier .md rentré dans le cmd en arg1, lecture et traduction
    with open(str(sys.argv[1]),'r', encoding="utf-8") as record:
        texte_fichier_md = record.read()
    texte_md_traduit = markdown(texte_fichier_md, extensions=['extra', 'codehilite', 'toc', 'sane_lists','md_in_html'])

    # si fichier = 'page_accueil.md' récupérer son css
    if sys.argv[1] == "page_accueil.md":
        with open('codehilite.css', 'r') as record:
            hilite_css = record.read()
        with open('main.css', 'r') as record:
            main_css = record.read()
        with open('fontawesome-all.min.css', 'r') as record:
            font_css = record.read()
    
    fichier_html = (
    """
    <!doctype html>
        <html lang="fr">
            <head>
                <meta charset="utf-8">
                <title>Titre de la page</title>
		        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
                <link rel="stylesheet" href="assets/css/main.css">
                <link rel="stylesheet" href="assets/css/hilite.css">
            </head>
            <body class="homepage">
                %s
            </body>
        </html>"""
        %(texte_md_traduit)
        )
    
    # try/catch pour créer un dossier nommé par le arg2, un fichier .html nommé par le arg1 rempli avec le .md + création d'un dossier 'assets'
    try:
        os.mkdir('../%s'%(sys.argv[2]))
        with open('../%s/index.html'%(sys.argv[2]),'w', encoding ="utf-8") as record:
            record.write(fichier_html)
        os.mkdir('../%s/assets'%(sys.argv[2]))

        # si arg1 = 'page_accueil.md' créer un dossier css et y mettre les css correspondant.
        if sys.argv[1] == "page_accueil.md":
            os.mkdir('../%s/assets/css'%(sys.argv[2]))
            with open('../%s/assets/css/hilite.css'%(sys.argv[2]),'w') as record:
                record.write(hilite_css)
            with open('../%s/assets/css/main.css'%(sys.argv[2]),'w') as record:
                record.write(main_css)
            with open('../%s/assets/css/fontawesome-all.min.css'%(sys.argv[2]),'w') as record:
                record.write(font_css)

    # renvoie l'erreur si présente
    except OSError as e:
        print(os.strerror(e.errno))
 
# appel de fonction
convert_and_create_static_site()