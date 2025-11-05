import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()
vitsi = vastaus['value']
print(vitsi)