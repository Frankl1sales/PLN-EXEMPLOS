from bs4 import BeautifulSoup

def extrair_comentarios(navegador):
    # Pegar a URL atual do navegador
    url = navegador.current_url

    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(navegador.page_source, 'html.parser')

    # Encontrar todos os blocos de comentários
    comentarios = soup.find_all('div', {'data-testid': 'review-description'})

    # Lista para armazenar os dados dos comentários
    dados_comentarios = []

    # Iterar sobre os blocos de comentários e extrair o nome e o comentário
    for comentario in comentarios:
        nome = comentario.find_previous('p', {'class': 'sc-kpDqfm eJPqHd sc-gNXrtx dBkwWm'}).text.strip()
        texto_comentario = comentario.text.strip()

        # Adicionar os dados do comentário à lista
        dados_comentarios.append({'nome': nome, 'comentario': texto_comentario})
        
    return dados_comentarios

from bs4 import BeautifulSoup

def extrair_informacoes_produto(navegador):
    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(navegador.page_source, 'html.parser')

    # Extrair o nome do produto
    nome_produto = soup.find('h1', {'data-testid': 'main-title'}).text.strip()

    # Extrair a nota média
    nota_media = soup.find('span', {'data-testid': 'review-totalizers-rating'}).text.strip()

    # Extrair o número de avaliações
    num_avaliacoes = soup.find('p', {'data-testid': 'review-totalizers-count'}).text.strip()

    # Extrair o total de comentários
    total_comentarios = soup.find('div', {'data-testid': 'review-total'}).text.strip()

    # Retornar as informações em um dicionário
    informacoes_produto = {
        'nome_produto': nome_produto,
        'nota_media': nota_media,
        'num_avaliacoes': num_avaliacoes,
        'total_comentarios': total_comentarios
    }

    return informacoes_produto
