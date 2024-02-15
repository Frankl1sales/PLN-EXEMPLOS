from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

# Obtém o caminho relativo ao diretório do script
arquivo_path = Path(__file__).resolve().parent / 'exemplo.html'

# Lê o conteúdo do arquivo HTML
with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Cria um objeto BeautifulSoup
soup = BeautifulSoup(conteudo, 'html.parser')

# Extrai o título da página
titulo = soup.title.string
print("Título da Página:", titulo)

# Extrai o texto do parágrafo
paragrafo = soup.p.string
print("Texto do Parágrafo:", paragrafo)

# Extrai os itens da lista não ordenada
itens_lista = soup.find_all('li')
print("Itens da Lista Não Ordenada:")
for item in itens_lista:
    print(item.string)

# Encontra todas as tags 'article'
articles = soup.find_all('article')

# Lista para armazenar informações
dados_articles = []

# Itera sobre as tags 'article' e extrai informações desejadas
for article in articles:
    # Verifica se a tag 'h3' existe no elemento 'article'
    h3_tag = article.find('h3')
    if h3_tag:
        titulo = h3_tag.text # extraí o texto
    else:
        titulo = "N/A"  # Se não encontrar a tag 'h3', atribui um valor padrão

    # Verifica se a tag 'p' existe no elemento 'article'
    p_tag = article.find('p')
    if p_tag:
        conteudo = p_tag.text # extraí o texto
    else:
        conteudo = "N/A"  # Se não encontrar a tag 'p', atribui um valor padrão

    # Adiciona as informações à lista
    dados_articles.append({'Título': titulo, 'Conteúdo': conteudo})

# Configurações para exibir o conteúdo completo das células
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', None)

# Cria um DataFrame do Pandas a partir da lista de informações
df = pd.DataFrame(dados_articles)

# Exibe o DataFrame
print(df)
