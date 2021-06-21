import requests
from getteams1 import teamId
url = "https://webexapis.com/v1/memberships?roomId={}".format(teamId)

payload={}
headers = {
  'Authorization': 'Bearer NWE4MDM2ZjAtMWJhMi00NDQzLWFlZDEtY2QzODBiOTc2NTY0OGYzMWQyOWYtYTkz_P0A1_6e31fd08-63c5-45b0-9a66-10c03c54016e'
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
