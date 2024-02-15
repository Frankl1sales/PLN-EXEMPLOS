import requests
from bs4 import BeautifulSoup

# URL da página
url = "https://www.magazineluiza.com.br/colchao-queen-molas-ensacadas-com-pillow-top-extra-conforto-158x198x38cm-premium-sleep-bf-colchoes/p/afebjggj35/co/ccbq/?&=&seller_id=emcompre"

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

        # Encontra o elemento HTML que contém o preço do produto
        price_element = soup.find("p", {"data-testid": "price-value"})

        if price_element:
            # Extrai e imprime o preço do produto
            price = price_element.text.strip()
            print("Preço do produto:", price)

            # Encontra o elemento HTML que contém o nível de estrelas dado pelos compradores
            stars_element = soup.find("span", {"data-testid": "review-totalizers-rating"})

            if stars_element:
                # Extrai e imprime o nível de estrelas
                stars = stars_element.text.strip()
                print("Nível de estrelas:", stars)

                # Encontra o elemento HTML que contém o número total de avaliações
                reviews_count_element = soup.find("p", {"data-testid": "review-totalizers-count"})

                if reviews_count_element:
                    # Extrai e imprime o número total de avaliações
                    reviews_count = reviews_count_element.text.strip().split()[0]
                    print("Número total de avaliações:", reviews_count)

                    # Encontra o elemento HTML que contém o número total de comentários
                    comments_total_element = soup.find("div", {"data-testid": "review-total"})

                    if comments_total_element:
                        # Extrai e imprime o número total de comentários
                        comments_total = comments_total_element.text.strip().split()[0]
                        print("Número total de comentários:", comments_total)
                    else:
                        print("Não foi possível encontrar o número total de comentários na página.")
                else:
                    print("Não foi possível encontrar o número total de avaliações na página.")
            else:
                print("Não foi possível encontrar o nível de estrelas na página.")
        else:
            print("Não foi possível encontrar o preço do produto na página.")
    else:
        print("Não foi possível encontrar o nome do produto na página.")
else:
    print("A requisição falhou com código de status:", response.status_code)
