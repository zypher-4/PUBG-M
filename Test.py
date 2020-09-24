import requests

url = f'http://192.168.0.174:10086/getteaminfolist'
r = requests.get(url)
data = r.json()
print(r)
