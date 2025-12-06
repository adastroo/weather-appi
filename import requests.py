import requests
# Dodawanie naszego klucza API
# API KEY PODMIENCIE NA SWOJ
api_key='c3f45f8793db4e23b1781213250612'
city='Warszawa'

#Utworzenie zapytania bezposrednio do strony internetowej OpenWeathermap
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes'


#Wykonuje zapytanie GET i pobierzemy dane w formacie JSON
response=requests.get(url)
response=response.json()

#Wyswietlamy pobrane dane
print(response)


