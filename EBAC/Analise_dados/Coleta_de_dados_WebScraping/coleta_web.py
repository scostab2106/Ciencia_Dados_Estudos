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


#Exibir textos das tags hw e p e a quantidade
for linha_texto in extracao.find_all(["h2", "P"]):
    if linha_texto.name == "h2":
        titulo = linha_texto.text.strip()
        print("Título: ", titulo)
        counth2 += 1
    elif linha_texto.name == "p":
        paragrafo = linha_texto.text.strip()
        print("Paragrafo: ", paragrafo)
        countp += 1
     

print("Quantidade de hs = ",counth2)
print("Quantidade de p = ", countp)
print("")

#Exibir tags aninhadas
for titulo in extracao.find_all("h2"):
    print("\n Título: ", titulo.text.strip())
    for link in titulo.find_next_siblings("p"):
        for a in link.find_all("a", href=True):
            print("Texto Link: ", a.text.strip(), " | URL:", a["href"])

