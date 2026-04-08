import requests


def enviar_arquivo():
    #Caminho do arquivo para upload
    caminho = 'C:/Users/samco/OneDrive/LP/Repositorios DEV/Arquivo aula API/arquivo teste.txt'

    server_resp = requests.get("https://api.gofile.io/servers")
    server_json = server_resp.json()
    server = server_json["data"]["servers"][0]["name"]


    #Enviar o arquivo
    requisicao = requests.post(url = f'https://{server}.gofile.io/uploadFile', files={'file': open(caminho, 'rb')} )

    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado, link para acesso: ", url)


def enviar_arquivo_acceskey():
    #Caminho do arquivo para upload
    caminho = 'C:/Users/samco/OneDrive/LP/Repositorios DEV/Arquivo aula API/arquivo teste.txt'
    chave_acesso = '...' #No lugar dos 3 pontos estaria uma API Key real

    server_resp = requests.get("https://api.gofile.io/servers")
    server_json = server_resp.json()
    server = server_json["data"]["servers"][0]["name"]


    #Enviar o arquivo
    requisicao = requests.post(
        url = f'https://{server}.gofile.io/uploadFile', 
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso} )

    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado, link para acesso: ", url)


def receber_arquivo(file_url):
    #Receber o arquivo
    requisicao = requests.get(file_url)

    #Salvar arquivo
    if requisicao.ok:
        with open('arquivo_baixado.txt', 'wb') as file:
            file.write(requisicao.content)
        print( "Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo: ", requisicao.json())


#enviar_arquivo()
receber_arquivo('https://gofile.io/d/O8T7HV')

