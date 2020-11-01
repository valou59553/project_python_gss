from markdown import markdown
import os, sys

def convert_and_create_static_site():
    with open('codehilite.css', 'r') as record:
        hilite_css = record.read()
    with open('main.css', 'r') as record:
        main_css = record.read()
    with open('fontawesome-all.min.css', 'r') as record:
        font_css = record.read()
    with open(str(sys.argv[1]),'r', encoding="utf-8") as record:
        texte_fichier_md = record.read()
    texte_md_traduit = markdown(texte_fichier_md, extensions=['extra', 'codehilite', 'toc', 'sane_lists'])

    fichier_html = (
    """
    <!doctype html>
        <html lang="fr">
            <head>
                <meta charset="utf-8">
                <title>Titre de la page</title>
                <link rel="stylesheet" href="assets/css/main.css">
                <link rel="stylesheet" href="assets/css/hilite.css">
            </head>
            <body>
                %s
            </body>
        </html>"""
        %(texte_md_traduit)
        )

    try:
        os.mkdir('../%s'%(sys.argv[2]))
        with open('../%s/site.html'%(sys.argv[2]),'w', encoding ="utf-8") as record:
            record.write(fichier_html)
        os.mkdir('../%s/assets'%(sys.argv[2]))
        os.mkdir('../%s/assets/css'%(sys.argv[2]))
        with open('../%s/assets/css/hilite.css'%(sys.argv[2]),'w') as record:
            record.write(hilite_css)
        with open('../%s/assets/css/main.css'%(sys.argv[2]),'w') as record:
            record.write(main_css)
        with open('../%s/assets/css/fontawesome-all.min.css'%(sys.argv[2]),'w') as record:
            record.write(font_css)
    except OSError as e:
        print(os.strerror(e.errno))

convert_and_create_static_site()