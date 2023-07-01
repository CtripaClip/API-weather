import requests
from requests import get

api = 'TOCEN' # your API tocen
lat = 42.56955
lon = 47.86447
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'

def request(url): # requests
    req = requests.get(url).json()
    print(req)

request(url) # call function
