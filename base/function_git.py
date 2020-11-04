import subprocess

def push_on_git():
    subprocess.run("git add ..", shell=True)
    subprocess.run("git commit -a -m 'dev'", shell=True)
    subprocess.run("git push", shell=True)