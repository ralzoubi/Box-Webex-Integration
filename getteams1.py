import requests

url = "https://webexapis.com/v1/memberships"

payload={}
headers = {
  'Authorization': 'Bearer '
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
#print(data)
for item in data['items']:
    teamId = item['roomId']

print("Webex Team ID: ", teamId)
