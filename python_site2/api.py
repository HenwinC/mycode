import requests

url = ""
data = requests.get(url).json()

for x in data:
    print(f"{x['name']} is a great weapon choice. Its weapon class is {x['class']}.")