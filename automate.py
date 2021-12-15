import json 
import requests
import subprocess

BASE_URL = "https://github.com/scalable-web-systems/"
f = open('config.json')
 
data = json.load(f)


for repo_name in data['repos']:
    print(repo_name)
    res = requests.get(BASE_URL+repo_name)
    if res.status_code != 200:
        print(repo_name, "does not exist or network error")
        continue
    subprocess.run(["git", "pull", BASE_URL+repo_name, "--allow-unrelated-histories"])

    
