from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt

def tokenizacao(texto):
    # Baixar a lista de stopwords se ainda não estiver disponível
    try:
        stopwords.words("portuguese")
    except LookupError:
        import nltk
        nltk.download('stopwords')

    # Tokenização
    tokens = word_tokenize(texto, language='portuguese')
    
    # Remover stopwords, vírgulas, pontos e espaços
    stop_words = set(stopwords.words('portuguese'))
    punctuation = set(string.punctuation)
    tokens_sem_stopwords = [token.lower() for token in tokens if token.lower() not in stop_words and token not in punctuation]

    return tokens_sem_stopwords

def exibir_informacoes_produto(informacoes_produto, n_comentarios):
    # Criar uma figura com subgráficos
    fig, ax = plt.subplots(figsize=(8, 6))

    # Adicionar as informações do produto como texto no subgráfico
    ax.text(0.5, 0.9, f"Nome do Produto: {informacoes_produto['nome_produto']}", ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.8, f"Nota Média: {informacoes_produto['nota_media']}", ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.7, f"Número de Avaliações: {informacoes_produto['num_avaliacoes']}", ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.6, f"Total de Comentários: {informacoes_produto['total_comentarios']}", ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.5, f"Número de comentários extraídos: {n_comentarios}", ha='center', va='center', transform=ax.transAxes)
    
    # Ajustar layout
    plt.tight_layout()


def tokens_mais_frequentes(textos_tokenizados):
    # Concatena todos os textos tokenizados
    todos_tokens = [token for texto in textos_tokenizados for token in texto]
    
    # Calcula a frequência das palavras
    freq_dist = FreqDist(todos_tokens)

    # Plota o gráfico de frequência das palavras
    freq_dist.plot(30, cumulative=False)


def processar_comentarios(dados_comentarios, informacoes_produto):
    for comentario in dados_comentarios:
        nome = comentario['nome']
        texto = comentario['comentario']
        numero_de_comentarios = len(dados_comentarios)

        # Aplicar tokenização e outras operações conforme necessário
        tokens_sem_stopwords = tokenizacao(texto)

        # Atualizar para armazenar os tokens sem stopwords
        comentario['comentario'] = tokens_sem_stopwords

        print(f"Nome: {nome}")
        print(f"Comentário: {tokens_sem_stopwords}")
        print("----")

    # Extrair tokens de todos os comentários
    textos_tokenizados = [comentario['comentario'] for comentario in dados_comentarios]

    # Analisar palavras mais utilizadas com as informações do produto
    exibir_informacoes_produto(informacoes_produto, numero_de_comentarios)
    tokens_mais_frequentes(textos_tokenizados)
    plt.show()
