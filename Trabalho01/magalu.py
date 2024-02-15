import requests
from bs4 import BeautifulSoup

# URL da página
url = "https://www.magazineluiza.com.br/apple-iphone-13-128gb-estelar-tela-61-12mp/p/234661900/te/ip13/"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status HTTP 200)
if response.status_code == 200:
    # Faz o parsing do HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra e imprime o título da página
    title = soup.title.string
    print("Título da página:", title)
else:
    print("A requisição falhou com código de status:", response.status_code)
