import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}

    for linha in artigo(['h3']):
        if linha.name == 'h3':
            titulo = (linha.text.strip())
            livro['Título'] = titulo

    for linha2 in artigo.find_all('p', class_='price_color'):
        if linha2.name == 'p':
            preco = (linha2.text.strip())
            livro['Preço'] = preco


    catalogo.append(livro)
    contar_livros += 1

print('Total livros:', contar_livros)
print (catalogo)
