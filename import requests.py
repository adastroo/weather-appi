import requests
# Dodawanie naszego klucza API
# API KEY PODMIENCIE NA SWOJ
api_key='c3f45f8793db4e23b1781213250612'

#wpisywanie miasta do zbierania pogody

city=input('podaj miasto dla ktorego chcesz wyswietlic pogode:')


user_choice=int(input(f'Wybierz, co chcesz wyświetlić dla {city}: '
                    f'
 1) Temperatura'
                    f'
 2) Ciśnienie'
                    f'
 3) Wilgotność'
                    f'
 4) Wszystkie informacje'
                    f'
 Twój wybór:'

))




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

