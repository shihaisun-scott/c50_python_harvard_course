# using APIs to get information on the internet

import requests # APIs
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent = 2)) # dump for pretty printing

o = response.json()
for result in o["results"]:
    print(result["trackName"])