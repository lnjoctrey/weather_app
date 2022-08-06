import requests as r

API_KEY = "ff556c8a56917d1b6a26df7cad50b4b0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = r.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Current Weather: ", weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Temperature: ", temperature, "celcius")
    
else:
    print("An error occurred")