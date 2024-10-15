import json

import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

response = requests.get(os.environ.get("ANNOUNCEMENT_API"))
events = response.json()["content"]["feeds"]

for i in events:
    contents = ""

    try:
        for j in json.loads(i['feed']["contents"])["document"]["components"][1]["value"]:
            contents += j['nodes'][0]['value']
    except:
        pass

    print(contents)
