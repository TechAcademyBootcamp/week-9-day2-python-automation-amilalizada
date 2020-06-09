import click
import os
import requests
import json

url = "https://api.github.com/user/repos"
headers={
    "Authorization": "token 7bbd9fa4088aaca0c1c422049ffab99db51edd51"
    }
payload={
    "name": "api_repo",
    }
    
x=requests.post(url,data=json.dumps(payload),headers=headers)
print(x.status_code)
@click.command()
@click.option('-p', '--project', required=True, help='acfad')
@click.option('--path', help='sdkjfds')
def create_project(project, path):
    html = None
    with open('index.html', 'r') as f:
        html = f.read()
    if path:
        os.chdir(path)
    os.mkdir(project)
    os.chdir(project)
    os.mkdir('css')
    os.mkdir('js')
    open('css/style.css', 'w').close()
    open('js/script.js', 'w').close()
    with open('index.html', 'w') as f:
        f.write(html)



    if click.confirm('git reponuz varmi? '):
        git_repo = click.prompt('repo unvani qeyd edin: ')
        os.system('git init')
        os.system(f'git remote add origin {git_repo}')
        os.system('git add .')
        os.system('git commit -m "project created"')
        os.system('git push origin master')

        



        

# 7bbd9fa4088aaca0c1c422049ffab99db51edd51

if __name__ == '__main__':
    create_project()