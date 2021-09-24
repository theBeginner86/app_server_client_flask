import requests

response = requests.get("http://localhost:5000/health")
if response.status_code == 200:
    print(response.json())



