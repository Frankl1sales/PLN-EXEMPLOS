import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

def extrair_valor(soup, elemento, atributo):
    valor = soup.find(elemento, {"data-testid": atributo})
    return valor.text.strip() if valor else None

def tokenizar_texto(texto):
    tokens = word_tokenize(texto)
     # Converte todos os tokens para minúsculas
    tokens = [token.lower() for token in tokens]
    # Remover vírgulas, pontos e espaços
    tokens = [token.strip('., ') for token in tokens]
    return tokens

def remover_stopwords(tokens):
    stop_words = set(stopwords.words('portuguese'))
    # Remover stopwords
    tokens = [token for token in tokens if token.lower() not in stop_words]
    return tokens

def analisar_palavras_mais_utilizadas(textos_tokenizados):
    # Concatena todos os textos tokenizados
    todos_tokens = [token for texto in textos_tokenizados for token in texto]
    
    # Calcula a frequência das palavras
    freq_dist = FreqDist(todos_tokens)

    # Plota o gráfico de frequência das palavras
    freq_dist.plot(30, cumulative=False)
    plt.show()


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

                # Tokenização usando a função atualizada
                tokens_nome = tokenizar_texto(nome_text)
                tokens_comentario = tokenizar_texto(comentario_text)
                # Remoção de stopwords usando a função atualizada
                tokens_comentario = remover_stopwords(tokens_comentario)
                # Adiciona um dicionário ao final da lista comentarios_produtos - duas chaves: nome e comentario
                comentarios_produtos.append({"Nome": tokens_nome, "Comentário": tokens_comentario})
                
            # Converte a lista de comentários em um DataFrame do Pandas
            df_comentarios = pd.DataFrame(comentarios_produtos)

            # Salva o DataFrame em um arquivo CSV
            output_path_comentarios = Path("comentarios_produtos.csv")
            df_comentarios.to_csv(output_path_comentarios, index=False)

            print(f"Os comentários dos produtos foram salvos em {output_path_comentarios}")

            # Analisa as palavras mais utilizadas nos comentários
            analisar_palavras_mais_utilizadas(df_comentarios['Comentário'])
        elif ver_comentario != 'n':
            print("Opção inválida. Não serão exibidos os comentários.")

    else:
        print(f"A requisição falhou com código de status: {response.status_code}")

# URL da página do primeiro produto
url_produto1 = "https://www.magazineluiza.com.br/apple-iphone-13-128gb-estelar-tela-61-12mp/p/234661900/te/ip13/"

# Extrai informações do primeiro produto
extrair_informacoes_produto(url_produto1)
