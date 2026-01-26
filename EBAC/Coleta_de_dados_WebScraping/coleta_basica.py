import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



url = "https://www.fundamentus.com.br/fii_resultado.php"
print("REQUESTS PURO")
print("")

#FAZER REQUISIÇÃO COMO USER_AGENT(COMO SE FOSSE O NAVEGADOR) pois esse site não está aceitando requisições do python por segurança
headers = {
    "User-Agent":"Chrome/120.0.0.0"
}

response = requests.get(url, headers=headers)
print(response.text)


print("BEAUTIFUL SOUP")
print("")
soup = bs(response.text, features= 'html.parser')
print(soup.prettify())


print("PANDAS")
print("")
url_dados = pd.read_html(response.text)
print (url_dados[0])