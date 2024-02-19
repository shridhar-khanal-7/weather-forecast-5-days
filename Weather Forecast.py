import requests

# city=str(input('Please enter the city name '))

# print(f'Displaying weather for {city}: ')

# url=f'https://wttr.in/{city}'
# result=requests.get(url)
# print(result.text)



#Note: I am using Open weather map API for forecasting the weather Data.

url='http://api.openweathermap.org/data/2.5/weather?'
city=str(input('Please enter the city name: '))
api_key='9706752e626b594995969d934a82bccf'

#api url for fetching weather data
api_url=f'{url}q={city}&appid={api_key}'

#Making the API request
response=requests.get(api_url)

if response.status_code==200:
    data_weather=response.json()
    Temperature=data_weather['main']['temp']
    description=data_weather['weather'][0]['description']
    humidity=data_weather['main']['humidity']
    wind_speed=data_weather['wind']['speed']

    print(f"\nFull Weather Information of{city} :")
    print(f'The temperature of {city} is {Temperature}°C.')
    print(f'The humidity of {city} is {humidity}%.')
    print(f'The wind speed of {city} is {wind_speed}m/s.')
    print(f'The weather of {city} is {description}.')
else:
    print("There is Error fetching the weather data. Please try again later.")

