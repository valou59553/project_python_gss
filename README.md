# project_python_gss
create gss
 
 # Installer git :
 
```bash
 sudo apt-get update .
```
 
```bash
 sudo apt-get install git.
```
 
# Si vous avez déjà git d'installer :
veuillez installer le projet sur votre ordinateur à l'aide de :

```bash
git clone https://github.com/valou59553/project_python_gss.git
```
ou
```bash
git clone git@github.com:valou59553/project_python_gss.git
```

Dans le dossier base, se trouve un dossier css et un dossier images, veuillez y mettre 
respectivement vos images et vos .css.
Les chemins de vos .md vers vos img doivent pointer vers './assets/images/nomimage.extension' ou 'assets/images/nomimage.extension'
Les chemins de vos .md vers vos css doivent pointer vers './assets/css/nomimage.css' ou 'assets/css/nomimage.css'
Le dossier comportant votre ou vos fichiers .md peut être flisser directement dans ce dossier base.

Veuillez aussi installer python au préalable :

```bash
 sudo apt-get update .
```

```bash
sudo apt-get install python3.8
```

Le reste des installations se fera automatiquement.

# Pour lancer le logiciel en ligne de commande :

Aller dans le dossier à l'aide de l'invite de commande avec "cd chemin_du_dossier/project_python_gss/base

puis 

```bash
python convertisseur.py nom_de_votre_dossier_contenant_les.md nom_du_dossier_a_créer
```
# ou (selon votre version python) :

```bash
python3 convertisseur.py nom_de_votre_dossier_contenant_les_md nom_du_dossier_a_créer
```
