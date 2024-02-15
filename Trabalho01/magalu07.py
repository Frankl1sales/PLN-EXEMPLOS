import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extrair_valor(soup, elemento, atributo):
    valor = soup.find(elemento, {"data-testid": atributo})
    return valor.text.strip() if valor else None

def tokenizar_texto(texto):
    return word_tokenize(texto)

def remover_stopwords(tokens):
    stop_words = set(stopwords.words('portuguese'))  # Lista de stopwords em português
    return [token for token in tokens if token.lower() not in stop_words]

def extrair_informacoes_produto(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        nome_produto = extrair_valor(soup, "h1", "heading-product-title")
        preco_produto = extrair_valor(soup, "p", "price-value")
        estrelas_produto = extrair_valor(soup, "span", "review-totalizers-rating")
        total_avaliacoes_produto = extrair_valor(soup, "p", "review-totalizers-count")
        total_comentarios_produto = extrair_valor(soup, "div", "review-total")

        print(f"Nome do produto: {nome_produto}")
        print(f"Preço do produto: {preco_produto}")
        print(f"Nível de estrelas: {estrelas_produto}")
        print(f"Número total de avaliações: {total_avaliacoes_produto}")
        print(f"Número total de comentários: {total_comentarios_produto}")

        ver_comentario = input("Deseja ver os comentários dos compradores? (s/n): ").lower()

        if ver_comentario == 's':
            nomes_comentarios = soup.find_all("p", class_="sc-kpDqfm eJPqHd sc-gNXrtx dBkwWm")
            comentarios = soup.find_all("div", {"data-testid": "review-description"})

            comentarios_produtos = []

            for nome, comentario in zip(nomes_comentarios, comentarios):
                nome_text = nome.text.strip()
                comentario_text = comentario.text.strip()

                # Tokenização usando a função separada
                tokens_nome = tokenizar_texto(nome_text)
                tokens_comentario = tokenizar_texto(comentario_text)
                # Remoção de stopwords
                tokens_comentario = remover_stopwords(tokens_comentario)
                comentarios_produtos.append({"Nome": tokens_nome, "Comentário": tokens_comentario})

    
            # Converte a lista de comentários em um DataFrame do Pandas
            df_comentarios = pd.DataFrame(comentarios_produtos)

            # Salva o DataFrame em um arquivo CSV
            output_path_comentarios = Path("comentarios_produtos.csv")
            df_comentarios.to_csv(output_path_comentarios, index=False)

            print(f"Os comentários dos produtos foram salvos em {output_path_comentarios}")

        elif ver_comentario != 'n':
            print("Opção inválida. Não serão exibidos os comentários.")

    else:
        print(f"A requisição falhou com código de status: {response.status_code}")

# URL da página do primeiro produto
url_produto1 = "https://www.magazineluiza.com.br/review/234661900/apple-iphone-13-128gb-estelar-tela-61-12mp/TE/IP13/?page=2"

# Extrai informações do primeiro produto
extrair_informacoes_produto(url_produto1)
