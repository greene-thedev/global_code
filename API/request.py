from pprint import pprint
import requests

api_key = '35583bf62e77ec0a6c99db66a3cbd9b8'
url = f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={api_key}'
get_requests = requests.get(url)

#print(get_requests.json())
output = get_requests.json()
print(output['wind'])
