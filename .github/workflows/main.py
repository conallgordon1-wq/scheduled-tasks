import requests
import smtplib

my_password = os.environ.get("MY_PASSWORD")
my_email = os.environ.get("MY_EMAIL")

api_key = os.environ.get("OWM_API_KEY")
lat = 53.3104
long = 6.2899

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    'cnt': 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data['list']:
    code = item['weather'][0]['id']
    if int(code) < 700:
        will_rain=True

if will_rain:
    print('Bring an umbrella!')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            # to_addrs=my_email,
            # to_addrs='sarahellenolan@gmail.com',
            to_addrs=os.environ.get('MY_TARGET_EMAIL'),
            msg='Bring an umbrella! It will rain in the next 12 hours.'
        )





