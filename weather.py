import requests
import datetime as dt

parameters= {
  'lat': 9.076479,
  'lng': 7.398574,
  'formatted': 0,
}

response= requests.get('https://api.sunrise-sunset.org/json', params= parameters)
response.raise_for_status()
data= response.json()
sunrise= data['results']['sunrise'].split("T")[1].split(":")[0]
sunset= data['results']['sunset'].split("T")[1].split(":")[0]

current_time= dt.datetime.now()

print(f'{sunrise}\n{sunset}')
print(current_time.hour)