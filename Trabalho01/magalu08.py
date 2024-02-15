import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixa as stopwords se ainda não estiverem instaladas
nltk.download('stopwords')

# Função para remover stopwords de um texto
def remover_stopwords(texto):
    stop_words = set(stopwords.words('portuguese'))
    tokens = word_tokenize(texto)
    tokens_sem_stopwords = [token for token in tokens if token.lower() not in stop_words]
    texto_sem_stopwords = ' '.join(tokens_sem_stopwords)
    return texto_sem_stopwords

# Texto de exemplo
texto_exemplo = "Este é um exemplo de frase com algumas palavras de parada."

# Remoção de stopwords no texto de exemplo
texto_sem_stopwords = remover_stopwords(texto_exemplo)

# Exibição dos resultados
print("Texto original:", texto_exemplo)
print("Texto sem stopwords:", texto_sem_stopwords)
