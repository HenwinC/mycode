import requests

url = "http://10.13.46.74:2225/jsondata"
data = requests.get(url)

print(data)

data= data.json()

for x in data:
    print(f"{x['name']} is considered the greatest player of all time. His favorite weapon is the {x['class']} and his playstle is {x['player_type']}")
