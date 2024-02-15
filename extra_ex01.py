from bs4 import BeautifulSoup
import pandas as pd

# Corrigindo o caminho do arquivo
arquivo_path = r'C:\temp\wp-github\PLN EXEMPLOS\Semana02\exemplo.html'

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
    # Verifica se a tag 'h2' existe no elemento 'article'
    h2_tag = article.find('h2')
    if h2_tag:
        titulo = h2_tag.text.strip()
    else:
        titulo = "N/A"  # Se não encontrar a tag 'h2', atribui um valor padrão

    # Verifica se a tag 'div' com a classe 'conteudo' existe no elemento 'article'
    div_conteudo = article.find('div', class_='conteudo')
    if div_conteudo:
        conteudo = div_conteudo.text.strip()
    else:
        conteudo = "N/A"  # Se não encontrar a tag 'div' com a classe 'conteudo', atribui um valor padrão

    # Adiciona as informações à lista
    dados_articles.append({'Título': titulo, 'Conteúdo': conteudo})

# Cria um DataFrame do Pandas a partir da lista de informações
df = pd.DataFrame(dados_articles)

# Exibe o DataFrame
print(df)
