import requests

url = "https://api.github.com"
response = requests.get(url)

if response.status_code == 200:
    print("Connexion à GitHub réussie ✅")
else:
    print(f"Erreur {response.status_code} ❌")
