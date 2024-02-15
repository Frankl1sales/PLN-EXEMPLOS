import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

# Função para extrair informações de um produto
def extrair_informacoes_produto(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_name_element = soup.find("h1", {"data-testid": "heading-product-title"})
        price_element = soup.find("p", {"data-testid": "price-value"})
        stars_element = soup.find("span", {"data-testid": "review-totalizers-rating"})
        reviews_count_element = soup.find("p", {"data-testid": "review-totalizers-count"})
        comments_total_element = soup.find("div", {"data-testid": "review-total"})

        product_name = product_name_element.text.strip() if product_name_element else None
        price = price_element.text.strip() if price_element else None
        stars = stars_element.text.strip() if stars_element else None
        reviews_count = reviews_count_element.text.strip().split()[0] if reviews_count_element else None
        comments_total = comments_total_element.text.strip().split()[0] if comments_total_element else None

        return {
            "Nome do produto": product_name,
            "Preço do produto": price,
            "Nível de estrelas": stars,
            "Número total de avaliações": reviews_count,
            "Número total de comentários": comments_total
        }

    return None

# Lista de URLs dos produtos
urls_produtos = [
    "https://www.magazineluiza.com.br/colchao-queen-molas-ensacadas-com-pillow-top-extra-conforto-158x198x38cm-premium-sleep-bf-colchoes/p/afebjggj35/co/ccbq/?&=&seller_id=emcompre",
    "https://www.magazineluiza.com.br/apple-iphone-13-128gb-estelar-tela-61-12mp/p/234661900/te/ip13/"
]

# Lista para armazenar os resultados
resultados = []

# Extrai informações de cada produto e adiciona à lista de resultados
for url_produto in urls_produtos:
    informacoes_produto = extrair_informacoes_produto(url_produto)
    if informacoes_produto:
        resultados.append(informacoes_produto)

# Converte a lista de resultados em um DataFrame do Pandas
df = pd.DataFrame(resultados)

# Salva o DataFrame em um arquivo ODS (LibreOffice)
output_path = Path("informacoes_produtos.ods")
df.to_excel(output_path, engine='odf', index=False)


print(f"As informações dos produtos foram salvas em {output_path}")
