from markdown import markdown
import os, sys, shutil, glob, webbrowser
from function_maj import maj_git, maj_pqt
from jinja2 import Environment, FileSystemLoader

# define var env for source and destination
if os.path.isdir('./%s'%sys.argv[1]) is True:
    env = {'source': sys.argv[1], 'destination': sys.argv[2]}
else:
    pass 

def open_website():    
    # open website on github, page index.html
    url = 'https://valou59553.github.io/project_python_gss/%s/index.html'%(env['destination'])
    webbrowser.open_new(url)

# fonction change name pour les nom de fichiers
def change_name_files(path, extension='.md'):
    return path.replace(extension, '').replace('./%s/'%(env['source']),'')

# fonction pour créer les dossiers présent de base au nouveau dossier
def create_folder(subfolder_name):
        src = './%s'%(subfolder_name)
        dst = '../%s/assets/%s'%(env['destination'], subfolder_name)   
        shutil.copytree(src=src ,dst=dst)

def convert_and_create_static_site(env):
    # ouverture du fichier .md rentré dans le cmd en arg1, lecture et conversion
    dossier_selection = glob.glob("./%s/*.md"%(env['source']))
    res = []
    for record in dossier_selection:  
        with open(record,'r', encoding="utf-8") as f:
            texte_fichier_md = f.read()
        res.append(markdown(texte_fichier_md, extensions=['extra','codehilite','toc','sane_lists','md_in_html','attr_list']))

    # enleve les .md et le chemin du fichier pour donner un nom lors de la création des fichiers .html
    name_files_end = []
    for record in dossier_selection: 
        name_files_end.append(change_name_files(record))

    # try/catch pour créer un dossier nommé par l'arg2, un fichier .html + création du dossier 'assets'
    try:
        # prendre le contenu des dossier images et css pour les replacer dans un assets dans le dossier 'arg2'
        create_folder('images')
        create_folder('css')

        # utilisation de jinja pour inserer le contenu du fichier traduit .md dans le body du fichier template.html
        template = Environment(loader=FileSystemLoader(searchpath='./')).get_template('template.html')
        fichier_html = []
        for i in range(len(dossier_selection)):
            fichier_html.append(template.render(texte_md_traduit = res[i]))
            # création du .html dans le dossier 'arg2'
            with open('../%s/%s.html'%(env['destination'], name_files_end[i]),'w', encoding ="utf-8") as record:
                record.write(fichier_html[i])

    # renvoie l'erreur si présente
    except OSError as e:
        print(os.strerror(e.errno))
 
# appel de fonctions
maj_pqt()
convert_and_create_static_site(env)
maj_git()
open_website()