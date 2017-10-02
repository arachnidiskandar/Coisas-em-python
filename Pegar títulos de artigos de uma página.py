from bs4 import BeautifulSoup
import requests

url = 'http://www.bbc.com/portuguese'
req = requests.get(url)
code_html = req.text
soup = BeautifulSoup(code_html, 'html.parser')      #deixa o código HTML da página de uma forma mais legível e guarda na variável.

#Dps disso, descobrir qual é a qual classe dos títulos dos artigos no cógido.

for title_link in soup.find_all(class_="title-link__title"): #Basicamente rodando por todos os "title_link__title e selecionando oq é título
    print(title_link.text)      #Imprimindo os títulos da página principal da BBC e usando ".text" para remover os links





