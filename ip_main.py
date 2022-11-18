import requests
import json
from datetime import datetime

response = requests.get("http://ip-api.com/json/")
result = json.loads(response.content)
print('IP [%s]: %s %s'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))
