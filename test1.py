
import requests, json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
IP = ''
KEY = ''

BASE_URL = "https://" + IP + "/api/config/event_sources/log_source_management/log_sources"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

url = BASE_URL
json_data = requests.get(url, headers=headers, verify=False).json()
#print (type(json_data))
#d=json_data[0]
#print(d['name'])


for log in json_data:
    print(f"Name:{log['name']} and  enabled: {log['enabled']}")
	#print (log.get("name"))
