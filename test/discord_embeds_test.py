import requests
import os
from dotenv import load_dotenv
import json
from pprint import pprint

load_dotenv()

headers = {
    "Content-Type": "application/json"
}

data = {
    "embeds": [
        {
            "title": f"제목",
            "description": f"내용",
            "url": f"https://www.naver.com",
            # "footer": {
            #     "icon_url": f"https://pbs.twimg.com/media/D_qCTf-UIAAdARi.jpg:large"
            # },
            "thumbnail": {
                "url": f"https://ibb.co/Nxhs1KG"
            }
        }
    ]
}

response = requests.post(os.environ.get("DISCORD_API"), headers=headers, data=json.dumps(data))
print(response.text)