from pyowm import OWM

api_key = "35583bf62e77ec0a6c99db66a3cbd9b8"

owm = OWM(api_key)

mgr = owm.weather_manager()

observation = mgr.weather_at_place('Ghana, ACC')

w = observation.weather

wind = w.wind()
humidity = w.humidity
rain = w.rain
atmosphere = w.detailed_status
temperature = w.temperature()

#try forecast.
#forecast = mgr.forecast_at_place('Ghana, CC', daily)

print(f"Wind: {wind}\n Humidity: {humidity}\n Rain: {rain}\n Atmospheric Conditions: {atmosphere}\n Temperature: {temperature}")
