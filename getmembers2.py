import requests
from getteams1 import teamId
url = "https://webexapis.com/v1/memberships?roomId={}".format(teamId)

payload={}
headers = {
  'Authorization': 'Bearer '
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
#print(data)
for item in data["items"]:
    personId = item["personId"]
    email = item["personEmail"]
    break
print("Person ID: ", personId)
print("Person Email: ", email)
