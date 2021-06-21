import requests

url = "https://webexapis.com/v1/rooms"

payload={}
headers = {
  'Authorization': 'Bearer NWE4MDM2ZjAtMWJhMi00NDQzLWFlZDEtY2QzODBiOTc2NTY0OGYzMWQyOWYtYTkz_P0A1_6e31fd08-63c5-45b0-9a66-10c03c54016e'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
data = response.json()
for item in data["items"]:
    roomName = item["title"]
    break
print("Room Name: ", roomName)
