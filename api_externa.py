import requests


url = "https://jsonplaceholder.typicode.com/users"


try:

    # Faz a requisição para a API
    resposta = requests.get(url, timeout=5)

    # Verifica se ocorreu algum erro HTTP
    resposta.raise_for_status()

    # Mostra o status da resposta
    print("Status:", resposta.status_code)

    # Converte a resposta para JSON
    dados = resposta.json()

    # Percorre os usuários
    for usuario in dados:
        print(usuario["name"], "-", usuario["email"])


except requests.exceptions.Timeout:

    print("Erro: a API demorou muito para responder.")


except requests.exceptions.ConnectionError:

    print("Erro: não foi possível conectar à API.")


except requests.exceptions.HTTPError as erro:

    print(f"Erro HTTP: {erro}")


except requests.exceptions.RequestException as erro:

    print(f"Erro na requisição: {erro}")


except ValueError:

    print("Erro: a resposta da API não está em formato JSON válido.")