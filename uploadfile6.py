import requests
from createfolder4 import folderId
import addcollaborator5

url = "https://upload.box.com/api/2.0/files/content"

headers = {

  'Authorization': 'Bearer XWk65QJ9oiQ3jcPAhmd3rPlpjp1tp2Ib',
  'Cookie': 'box_visitor_id=60c6a289be7b72.52458416; site_preference=desktop'
}
# put folder id as id

files = {
    'attributes': [None, '{"name":"cc.pptx", "parent":{"id":"%s"}}'% folderId] ,
    'file': ('cc.pptx', open('/Users/ruqia/Downloads/boxwebex/cc.pptx', 'rb')),
}

response = requests.post('https://upload.box.com/api/2.0/files/content', headers=headers, files=files)
print(response.json())
