import requests

url = "https://webexapis.com/v1/rooms"

payload={}
headers = {
  'Authorization': 'Bearer '
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
data = response.json()
for item in data["items"]:
    roomName = item["title"]
    break
print("Room Name: ", roomName)
