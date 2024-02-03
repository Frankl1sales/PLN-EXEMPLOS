"""
Problema 2 ✅: Peça ao usuário para inserir uma frase ou uma palavra. 
Em seguida, crie um programa que conte quantas vogais e consoantes 
estão presentes na entrada. Exiba os resultados.
"""

s1 = input("Digite uma frase: ")
def contadorVogaisConsoantes(s1):
    vogais = "aeiouAEIOU"
    cont_vogais = 0
    cont_consoantes = 0

    for char in s1: 
      if char.isalpha(): # verifica se o caracter é alfanumerico
        if char in vogais:
          cont_vogais += 1
        else:
          cont_consoantes += 1
    return cont_vogais, cont_consoantes

vogais, consoantes = contadorVogaisConsoantes(s1)
print("numero de vogais: ", vogais)
print("numero de consoantes ", consoantes)