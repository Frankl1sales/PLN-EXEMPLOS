import math

def calcular_entropia(palavra):
  # Converte a palavra para uma lista de caracteres.
  caracteres = list(palavra)

  # Cria um dicionário para armazenar a frequência de cada caractere.
  frequencias = {}
  for caractere in caracteres:
    if caractere not in frequencias:  # Se não estiver presente é adicionado e atribui 0 para inicialização
      frequencias[caractere] = 0
    frequencias[caractere] += 1 # Depois é adicionado 1 para a ocorrência do caractere

  # Calcula a entropia da palavra.
  entropia = 0
  for caractere, frequencia in frequencias.items():
    probabilidade = frequencia / len(caracteres)
    entropia += -probabilidade * math.log2(probabilidade)
    return entropia

# Executa o algoritmo para as palavras fornecidas.
palavras = ["ARARAQUARA", "UFPEL", "PELOTAS", "FLORESTA", "COMPUTADOR"]
for palavra in palavras:
  entropia = calcular_entropia(palavra)
  print(f"Entropia de '{palavra}': {entropia:.4f}")
