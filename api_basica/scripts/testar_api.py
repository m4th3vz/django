import requests

# URL da sua API
url = 'http://localhost:8000/meu-endpoint/'

# Dados para enviar no POST
dados = {
    'nome': 'Matheus'
}

# Fazendo a requisição POST
response = requests.post(url, json=dados)

# Mostrando a resposta
print(response.json())
