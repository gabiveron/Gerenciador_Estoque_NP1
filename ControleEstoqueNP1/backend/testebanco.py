import requests

url = "http://localhost:8000"

dados = {
    "id_produto": 2,
    "quantidade": 5,
    "tipo": "ENTRADA"
}

resposta = requests.post(url + "/movimentacoes", json=dados)
print("POST MOVIMENTAÇÃO:", resposta.status_code)
print(resposta.json())