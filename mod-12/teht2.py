import requests

API_AVAIN = "api-avain"

paikkakunta = input("Paikkakunta: ")

params = {
        'q': paikkakunta,
        'appid': API_AVAIN,
        'lang': 'fi'
    }

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

data = response.json()

kuvaus = data['weather'][0]['description']
lampotila_kelvin = data['main']['temp']

lampotila_celsius = lampotila_kelvin - 273.15

print(f"Säätila ( {paikkakunta.capitalize()} ): {kuvaus.capitalize()}")
print(f"Lämpötila: {lampotila_celsius:.2f} °C")


