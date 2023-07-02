import requests
from requests import get

api = 'TOCEN' # settings
lat = 42.56955
lon = 47.86447

city = "Armavir"

url = f'https://api.openweathermap.org/data/2.5/weather?name={city}&appid={api}' # links
url2 = f'https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={api}'

def request(url): # requests

    def weather_now():
        req = requests.get(url).json()
        print(req)

    def weather30():
        req2 = requests.get(url2).json()
        print(req2)

if __name__ == '__main__':
    request(url).weath # call function
