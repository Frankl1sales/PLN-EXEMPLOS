import instaloader
import requests
from bs4 import BeautifulSoup

# Função para obter os comentários de uma postagem
def obter_comentarios(post_url):
    # Obter o conteúdo HTML da página
    response = requests.get(post_url)
    html = response.text

    # Analisar o HTML usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar elementos que contêm os comentários
    comentarios_html = soup.find_all('div', {'class': 'C4VMK'})

    # Extrair texto dos elementos de comentário
    comentarios = [comentario.get_text() for comentario in comentarios_html]

    return comentarios

# URL do post no Instagram
post_url = 'https://www.instagram.com/p/C1mKc1gstNH/'

# Obter comentários usando a função
comentarios = obter_comentarios(post_url)

# Imprimir os comentários
for i, comentario in enumerate(comentarios, start=1):
    print(f"Comentário {i}: {comentario}")
