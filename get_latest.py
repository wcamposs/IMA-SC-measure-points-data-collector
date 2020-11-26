from http import HTTPStatus
import json
import os

import requests
import pendulum


# Realizando requisição ao site do IMA para obter os dados publicados
resp = requests.get("https://balneabilidade.ima.sc.gov.br/relatorio/mapa")

# Verificando se a requisição deu certo, caso contrário sai do script
if not resp.status_code == HTTPStatus.OK:
    quit()

# Abre ponteiro de leitura e escrita do arquivo latest.json para receber os dados do buffer da requisição
with open("latest.json", "w+") as f:
    # Executa a escrita dos dados e formata para ficar legível utilizando json.dumps()
    f.write(json.dumps(resp.json(), indent=4))

    # Nome do arquivo para armazenar o histórico
    filename = "{}.json".format(pendulum.now().strftime("%Y-%m-%d"))

    # Copiando o arquivo gerado no momento da requisição para o arquivo
    os.system(f"cp latest.json ./data/{filename}") 




