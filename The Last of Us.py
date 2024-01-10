import requests
from bs4 import BeautifulSoup

cabecalho = {'user-agent': 'Mozilla/5.0'}
response = requests.get('https://www.adorocinema.com/series-tv/melhores/decada-2020/ano-2023/',
                          headers = cabecalho)
response.text

janta_01 = response.text
janta_01

janta_02 = BeautifulSoup(janta_01,'html.parser')
lista_de_filmes = janta_02.find_all("h2",class_="meta-title")
listagem_de_resumo = janta_02.find_all('div',class_="synopsis")
listagem_de_classificação = janta_02.find_all('div',class_="meta-body-item meta-body-info")
listagem_de_atores = janta_02.find_all('div',class_="meta-body-item meta-body-actor")
proxima_pagina = janta_02.find("span",class_="txt")


nome = lista_de_filmes[2]
nome_de_filme = nome.find("a",class_="meta-title-link").get_text().strip()

texto = listagem_de_resumo[2]
synopsis_01 = texto.find('div',class_='content-txt').get_text().strip()

para_1 = listagem_de_classificação[2]
categoria_01 = para_1.find("span").get_text().strip()

principais_01 = listagem_de_atores[2]
atores_p_01 = principais_01.find("span").get_text().strip()



print ("NOME DO FILME")
print (nome)

  
print ("CLASSIFICAÇÃO")
print (para_1)

print ("ELENCO")
print (principais_01)

print ("SYNOPSIS")
print (texto)



