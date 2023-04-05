import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'income':50000, 'age':20, 'rooms':7})

print(r.json())