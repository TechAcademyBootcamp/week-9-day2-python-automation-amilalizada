import os
import json
os.system('virtualenv .venv')
os.system('source .venv/bin/activate')
os.system("pip install requests")
os.system('pip install click')
import requests
import click

url = "https://api.github.com/user/repos"
headers={
    "Authorization": "token 7bbd9fa4088aaca0c1c422049ffab99db51edd51"
    }
payload={
    "name": "api_repo_second",
    }
x=requests.post(url,data=json.dumps(payload),headers=headers)
@click.command()
@click.option('-p', '--project', required=True, help='acfad')
@click.option('--path', help='sdkjfds')
def create_project(project, path):
    if path:
        os.chdir(path)
    os.mkdir(project)
    os.chdir(project)
    os.mkdir('python_notes')
    open('python_notes/notes.txt', 'w').close()

    if click.confirm('git reponuz varmi? '):
        git_repo = click.prompt('repo unvani qeyd edin: ')
        os.system('git init')
        os.system(f'git remote add origin {git_repo}')
        os.system('git add .')
        os.system('git commit -m "project created"')
        os.system('git push origin master')


if __name__ == '__main__':
    create_project()


