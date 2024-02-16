import requests
from bs4 import BeautifulSoup

# URL da página
url = "https://www.magazineluiza.com.br/review/ecadg9ee4f/colchao-magnetico-queen-bio-massageador-eco-prince-eco-new-colchoes/CO/CCBQ/"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status HTTP 200)
if response.status_code == 200:
    # Faz o parsing do HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra o elemento HTML que contém o nome do produto
    product_name_element = soup.find("h1", {"data-testid": "heading-product-title"})

    if product_name_element:
        # Extrai e imprime o nome do produto
        product_name = product_name_element.text.strip()
        print("Nome do produto:", product_name)

        # Encontra todos os elementos HTML que contêm os nomes dos comentários
        names_elements = soup.find_all("p", {"class": "sc-kpDqfm eJPqHd sc-gNXrtx dBkwWm"})

        # Encontra todos os elementos HTML que contêm os comentários
        comments_elements = soup.find_all("div", {"data-testid": "review-description"})

        # Itera sobre os elementos para extrair e imprimir os nomes e comentários
        for name_element, comment_element in zip(names_elements, comments_elements):
            name = name_element.text.strip()
            comment = comment_element.text.strip()
            print(f"Nome do comentário: {name}\nComentário: {comment}\n---")

    else:
        print("Não foi possível encontrar o nome do produto na página.")
else:
    print("A requisição falhou com código de status:", response.status_code)
