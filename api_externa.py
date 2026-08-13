import requests

url = "https://jsonplaceholder.typicode.com/users"

resposta = requests.get(url)

print("Status:", resposta.status_code)

dados = resposta.json()

for usuario in dados:
    print(usuario["name"], "-", usuario["email"])