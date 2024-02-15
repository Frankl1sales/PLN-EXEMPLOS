import requests
from bs4 import BeautifulSoup

def extrair_informacoes_produto(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        def extrair_valor(elemento, atributo):
            valor = soup.find(elemento, {"data-testid": atributo})
            return valor.text.strip() if valor else None

        nome_produto = extrair_valor("h1", "heading-product-title")
        preco_produto = extrair_valor("p", "price-value")
        estrelas_produto = extrair_valor("span", "review-totalizers-rating")
        total_avaliacoes_produto = extrair_valor("p", "review-totalizers-count")
        total_comentarios_produto = extrair_valor("div", "review-total")

        print(f"Nome do produto: {nome_produto}")
        print(f"Preço do produto: {preco_produto}")
        print(f"Nível de estrelas: {estrelas_produto}")
        print(f"Número total de avaliações: {total_avaliacoes_produto}")
        print(f"Número total de comentários: {total_comentarios_produto}")

        ver_comentario = input("Deseja ver os comentários dos compradores? (s/n): ").lower()

        if ver_comentario == 's':
            nomes_comentarios = soup.find_all("p", class_="sc-kpDqfm eJPqHd sc-gNXrtx dBkwWm")
            comentarios = soup.find_all("div", {"data-testid": "review-description"})

            for nome, comentario in zip(nomes_comentarios, comentarios):
                print(f"Nome do comentário: {nome.text.strip()}\nComentário: {comentario.text.strip()}\n---")

        elif ver_comentario != 'n':
            print("Opção inválida. Não serão exibidos os comentários.")

    else:
        print(f"A requisição falhou com código de status: {response.status_code}")

# URL da página do primeiro produto
url_produto1 = "https://www.magazineluiza.com.br/colchao-queen-molas-ensacadas-com-pillow-top-extra-conforto-158x198x38cm-premium-sleep-bf-colchoes/p/afebjggj35/co/ccbq/?&=&seller_id=emcompre"

# Extrai informações do primeiro produto
extrair_informacoes_produto(url_produto1)
