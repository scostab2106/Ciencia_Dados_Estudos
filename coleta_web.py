import requests
from bs4 import BeautifulSoup

url = "http://python.org.br/web/"

requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features= "html.parser")

#Exibir o texto
print(extracao.text.strip()) #Strip = remover espaços em bracno


#Filtrar exibição pela tag
counth2 = 0
countp = 0

for linha_texto in extracao.find_all("h2"):
    titulo = linha_texto.text.strip()
    print("Título: ", titulo)
    counth2 += 1

for linha_texto in extracao.find_all("p"):
    p = linha_texto.text.strip()
    print("P: ", titulo)
    countp = countp + 1

print("Quantidade de hs = ",counth2)
print("Quantidade de p = ", countp)