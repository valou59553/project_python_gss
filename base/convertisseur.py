from markdown import markdown
import os, sys, shutil
from jinja2 import Environment, FileSystemLoader

def convert_and_create_static_site():
    # ouverture du fichier .md rentré dans le cmd en arg1, lecture et conversion
    with open(str(sys.argv[1]),'r', encoding="utf-8") as record:
        texte_fichier_md = record.read()
    texte_md_traduit = markdown(texte_fichier_md, extensions=['extra', 'codehilite', 'toc', 'sane_lists','md_in_html'
                                                            ,'attr_list'])
    
    # utilisation de jinja pour inserer le contenu du fichier traduit .md dans le body du fichier template.html
    env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = env.get_template('template.html')
    fichier_html = template.render(texte_md_traduit=texte_md_traduit)
    
    # try/catch pour créer un dossier nommé par l'arg2, un fichier .html + création du dossier 'assets'
    try:
        # prendre le contenu des dossier images et css pour les replacer dans un assets dans le dossier 'arg2'
        src = './images'
        dst = '../%s/assets/images'%(sys.argv[2])   
        shutil.copytree(src=src ,dst=dst)

        src = './css'
        dst = '../%s/assets/css'%(sys.argv[2]) 
        shutil.copytree(src=src ,dst=dst)
        # création du .html dans le dossier 'arg2'
        with open('../%s/index.html'%(sys.argv[2]),'w', encoding ="utf-8") as record:
            record.write(fichier_html)

    # renvoie l'erreur si présente
    except OSError as e:
        print(os.strerror(e.errno))
 
# appel de fonction
convert_and_create_static_site()