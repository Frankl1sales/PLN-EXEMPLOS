import requests
from bs4 import BeautifulSoup

# URL da página do primeiro produto
url_produto1 = "https://www.magazineluiza.com.br/colchao-queen-molas-ensacadas-com-pillow-top-extra-conforto-158x198x38cm-premium-sleep-bf-colchoes/p/afebjggj35/co/ccbq/?&=&seller_id=emcompre"

# Faz a requisição GET para o primeiro produto
response_produto1 = requests.get(url_produto1)

# Verifica se a requisição foi bem-sucedida (código de status HTTP 200)
if response_produto1.status_code == 200:
    # Faz o parsing do HTML usando BeautifulSoup
    soup_produto1 = BeautifulSoup(response_produto1.text, 'html.parser')

    # Encontra o elemento HTML que contém o nome do produto
    product_name_element_produto1 = soup_produto1.find("h1", {"data-testid": "heading-product-title"})

    if product_name_element_produto1:
        # Extrai e imprime o nome do produto
        product_name_produto1 = product_name_element_produto1.text.strip()
        print("Nome do produto (Produto 1):", product_name_produto1)

        # Encontra o elemento HTML que contém o preço do produto
        price_element_produto1 = soup_produto1.find("p", {"data-testid": "price-value"})

        if price_element_produto1:
            # Extrai e imprime o preço do produto
            price_produto1 = price_element_produto1.text.strip()
            print("Preço do produto (Produto 1):", price_produto1)

            # Encontra o elemento HTML que contém o nível de estrelas dado pelos compradores
            stars_element_produto1 = soup_produto1.find("span", {"data-testid": "review-totalizers-rating"})

            if stars_element_produto1:
                # Extrai e imprime o nível de estrelas
                stars_produto1 = stars_element_produto1.text.strip()
                print("Nível de estrelas (Produto 1):", stars_produto1)

                # Encontra o elemento HTML que contém o número total de avaliações
                reviews_count_element_produto1 = soup_produto1.find("p", {"data-testid": "review-totalizers-count"})

                if reviews_count_element_produto1:
                    # Extrai e imprime o número total de avaliações
                    reviews_count_produto1 = reviews_count_element_produto1.text.strip().split()[0]
                    print("Número total de avaliações (Produto 1):", reviews_count_produto1)

                    # Encontra o elemento HTML que contém o número total de comentários
                    comments_total_element_produto1 = soup_produto1.find("div", {"data-testid": "review-total"})
                    
                    if comments_total_element_produto1:
                        # Extrai e imprime o número total de comentários
                        comments_total_produto1 = comments_total_element_produto1.text.strip().split()[0]
                        print("Número total de comentários (Produto 1):", comments_total_produto1)

                        # Encontra o elemento HTML que contém o nome do produto (segunda requisição)
                        product_name_element = soup_produto1.find("h1", {"data-testid": "heading-product-title"})
                        ver_comentario = input("Deseja ver os comentários dos compradores? (s/n): ").lower()
                        if ver_comentario == 's':
                            if product_name_element:
                                # Extrai e imprime o nome do produto (segunda requisição)
                                product_name = product_name_element.text.strip()
                                print("COMENTÁRIOS EXTRAÍDOS:")

                                # Encontra todos os elementos HTML que contêm os nomes dos comentários
                                names_elements = soup_produto1.find_all("p", {"class": "sc-kpDqfm eJPqHd sc-gNXrtx dBkwWm"})

                                # Encontra todos os elementos HTML que contêm os comentários
                                comments_elements = soup_produto1.find_all("div", {"data-testid": "review-description"})

                                # Itera sobre os elementos para extrair e imprimir os nomes e comentários
                                for name_element, comment_element in zip(names_elements, comments_elements):
                                    name = name_element.text.strip()
                                    comment = comment_element.text.strip()
                                    print(f"Nome do comentário: {name}\nComentário: {comment}\n---")
                            else:
                                print("Não foi possível encontrar o nome do produto na página.")
                        elif ver_comentario != 'n':
                                print("Oção invalida. Não serão exibidos os comentários")
                        else:
                            print("A requisição falhou com código de status:", response_produto1.status_code)
                    else:
                        print("Não foi possível encontrar o número total de comentários na página (Produto 1).")
                else:
                    print("Não foi possível encontrar o número total de avaliações na página (Produto 1).")
            else:
                print("Não foi possível encontrar o nível de estrelas na página (Produto 1).")
        else:
            print("Não foi possível encontrar o preço do produto na página (Produto 1).")
    else:
        print("Não foi possível encontrar o nome do produto na página (Produto 1).")
else:
    print("A requisição falhou com código de status:", response_produto1.status_code)
