"""
Problema 6 ✅: Remoção de stopwords: Remova as palavras de parada (stopwords) 
do texto. Você pode usar a lista de stopwords do NLTK ou outra 
lista de sua escolha.
"""

import spacy
import nltk
from nltk.corpus import stopwords

# Carrega o modelo SpaCy
nlp = spacy.load('pt_core_news_sm')

# Texto de exemplo
texto = """Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a
floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e
folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas
estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira
onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não
resistiram à tentação de experimentar os doces. Mas, assim que começaram a
comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os
assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A
bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente,
após uma longa e cansativa jornada, João e Maria voltaram em segurança para
sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa."""

# Tokenização do texto usando SpaCy
doc = nlp(texto)

# Lista de stopwords do NLTK
stopwords_nltk = set(stopwords.words('portuguese'))

# Remove as stopwords do texto
palavras_sem_stopwords = [token.text for token in doc if token.text.lower() not in stopwords_nltk]

# Exibe as palavras após a remoção das stopwords
print(palavras_sem_stopwords)
print("\n")
print(len(palavras_sem_stopwords))
