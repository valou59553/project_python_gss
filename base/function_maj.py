import subprocess

def maj_git():
    subprocess.run("git pull", shell=True)
    subprocess.run("git add ..", shell=True)
    subprocess.run("git commit -a -m 'dev'", shell=True)
    subprocess.run("git push", shell=True)

def maj_pqt():
    subprocess.run("sudo apt-get upgrade", shell=True)
    subprocess.run("pip install -r requirements.txt", shell=True)
    subprocess.run("pip3 install -r requirements.txt", shell=True)