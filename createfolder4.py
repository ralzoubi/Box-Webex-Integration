import requests
import json
import getmembers2
from getroomname3 import roomName

url = "https://api.box.com/2.0/folders"

payload = json.dumps({
  "name": "%s",
  "parent": {
    "id": "0"
  },
  "folder_upload_email": {
    "access": "open"
  },
  "sync_state": "synced"
}) % roomName
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer XWk65QJ9oiQ3jcPAhmd3rPlpjp1tp2Ib',
  'Cookie': 'box_visitor_id=60c6a289be7b72.52458416'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
data = response.json()
#print(data)
for k,v in data.items():
    if k == "id":
        folderId = v
# print(data)
print("Folder ID: ", folderId)
