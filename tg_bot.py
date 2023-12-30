import requests
import json


response = json.loads(requests.get("https://api.telegram.org/bot6329190450:AAFgRw8vj8pqTpamCOwN-unTUZIxyW03fds/getMe").text)
chat = json.loads(requests.get("https://api.telegram.org/bot6329190450:AAFgRw8vj8pqTpamCOwN-unTUZIxyW03fds/getUpdates").text)

message = requests.get(f"https://api.telegram.org/bot6329190450:AAFgRw8vj8pqTpamCOwN-unTUZIxyW03fds/sendMessage?chat_id={chat['result'][0]['message']['chat']['id']}&text=asdasd")
