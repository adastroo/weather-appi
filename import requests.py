import requests
# Dodawanie naszego klucza API
# API KEY PODMIENCIE NA SWOJ
api_key='c3f45f8793db4e23b1781213250612'

#wpisywanie miasta do zbierania pogody

city=input('podaj miasto dla ktorego chcesz wyswietlic pogode:')


input_message=(f'Wybierz, co chcesz wyświetlić dla {city}: '
f'\n 1) Temperatura'
f'\n 2) Ciśnienie'
f'\n 3) Wilgotność'
f'\n 4) Wszystkie informacje'
f'\n Twój wybór:')




user_choice=int(input(input_message))

#zabezpieczenie przed wpisaniem wartosci innej niz z zakresu 1-4
#wpisanie wartosci do momentu wlasciwego
while user_choice>4 or user_choice<1:
    print('nieprawidlowa wartosc')
    #ponowne wpisanie
    user_choice=int(input(input_message))

#Utworzenie zapytania bezposrednio do strony internetowej OpenWeathermap
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes'


#Wykonuje zapytanie GET i pobierzemy dane w formacie JSON
response=requests.get(url)
response=response.json()

#Wyswietlamy pobrane dane
#print(response)

#wyswietlanie w zaleznosci od inputu


if user_choice==1:
    print(f"Temperatura dla miasta {city} wynosi  {response['current']['temp_c']} stopni.")
elif user_choice==2: 
    print(f"Ciśnienie dla miasta {city} wynosi  {response['current']['pressure_mb']}.")
elif user_choice==3:
    print(f"Wilgotność dla miasta {city} wynosi  {response['current']['humidity']}.")
elif user_choice==4:
    print(f"Temperatura dla miasta {city} wynosi  {response['current']['temp_c']} stopni.")
    print(f"Ciśnienie dla miasta {city} wynosi  {response['current']['pressure_mb']}.")
    print(f"Wilgotność dla miasta {city} wynosi  {response['current']['humidity']}.")
    #Informacje ogólne o pogodzie
    weather_condition= response['current']['condition']['text']
    print(f"Stan pogody w {city} to {weather_condition}.")
else:
    print("Nieprawidłowy wybór.")

