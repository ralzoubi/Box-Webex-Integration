import requests
import json
from createfolder4 import folderId
from getmembers2 import personId
from getmembers2 import email

url = "https://api.box.com/2.0/collaborations"
payload = json.dumps({
  "item": {
    "type": "folder",
    "id": "%s"
  },
   "accessible_by": {
     "type": "user",
    "id": "16344142330",
    "login": "%s"
  },
  "role": "editor",
  "can_view_path": True,
  "expires_at": "2022-08-29T23:59:00-07:00"
}) % (folderId, email)
print(payload)
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer XWk65QJ9oiQ3jcPAhmd3rPlpjp1tp2Ib',
  'Cookie': 'box_visitor_id=60c6a289be7b72.52458416; site_preference=desktop'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.json())
