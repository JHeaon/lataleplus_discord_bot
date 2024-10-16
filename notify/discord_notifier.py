import requests
import json
import os
from dotenv import load_dotenv
from notify.notifier import Notifier

load_dotenv()


class DiscordNotifier(Notifier):

    def push(self, data_list):
        discord_api = self.url

        for data in data_list[::-1]:
            headers = {
                "Content-Type": "application/json"
            }

            json_data = {
                "embeds": [
                    {
                        "title": f"{data.title}",
                        "description": f"{data.contents}",
                        "url": f"{data.url}",
                        "thumbnail": {
                            "url": f"{os.environ.get("FREERLING_IMG")}"
                        }
                    }
                ]
            }

            requests.post(discord_api, headers=headers, data=json.dumps(json_data))

    def send_message(self, message):
        discord_api = self.url

        headers = {
            "Content-Type": "application/json"
        }

        json_data = {
            'content': message
        }

        requests.post(discord_api, headers=headers, data=json.dumps(json_data))
