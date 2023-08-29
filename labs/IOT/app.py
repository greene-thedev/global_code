# importing package for making api requests
import requests
# importing GPIO packages
from gpiozero import Button
from signal import pause

# making API call a function
def get_url():
    url = "https://maker.ifttt.com/trigger/notification/json/with/key/lxi_09_iTWs-6l0Avj5SsFUOk0X7GuK3mHeVKH_9GbT"
    r = requests.get(url)
    print(r)

# giving the button logic    
button = Button(2)
button.when_pressed = get_url

# don't forget to pause... Import it first though.
pause()