import requests
import json
from requests.auth import HTTPBasicAuth

def get_data():
    response = requests.request(
       "GET",
       url,
       auth=HTTPBasicAuth(app_user_name, app_pass)
    )
    
    return json.loads(response.text)

url = "https://api.bitbucket.org/2.0/repositories/workspacename"
app_pass = "********"
app_user_name = "**********"
    
json_data = get_data()

repos = []
    
first_pass = True
condition = False
while first_pass or condition:
    first_pass = False
    for repo in json_data["values"]:
        print(repo["full_name"])
        repos.append(repo["full_name"].replace("workspacename/", ""))
    if not (json_data.get('next') is None):
        url = json_data["next"]
        json_data = get_data()
        condition = True
    else:
        condition = False
        
print(sorted(repos))
