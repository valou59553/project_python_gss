import subprocess

def push_on_git():
    subprocess.run("git add .")
    subprocess.run("git commit -a -m 'dev'")
    subprocess.run("git push")