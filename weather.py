import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    res = requests.get(url)
    print(res.text)

get_weather("Tashkent")
