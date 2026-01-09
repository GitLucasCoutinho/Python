import requests
import json

# URL da API de localidades do IBGE (lista de estados)
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

try:
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        # Imprime os dados formatados em JSON
        print(json.dumps(dados, indent=4, ensure_ascii=False))

        # Exemplo: mostrar apenas nome e sigla dos estados
        print("\nLista de estados:")
        for estado in dados:
            print(f"{estado['sigla']} - {estado['nome']}")
    else:
        print("Erro na requisição. Código:", resposta.status_code)

except Exception as e:
    print("Ocorreu um erro:", e)