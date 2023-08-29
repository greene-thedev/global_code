import requests

url = "https://maker.ifttt.com/trigger/notification/json/with/key/lxi_09_iTWs-6l0Avj5SsFUOk0X7GuK3mHeVKH_9GbT"

r = requests.get(url)

print(r)