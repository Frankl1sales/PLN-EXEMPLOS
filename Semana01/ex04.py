"""
Problema 4: Peça ao usuário para inserir uma frase. 
Seu programa deve encontrar e exibir a palavra mais longa na frase. 
Você pode considerar que as palavras são separadas por espaços em branco. 
Por exemplo, se o usuário inserir "Python é uma linguagem de programação poderosa", 
o programa deve exibir "programação" como a palavra mais longa.
"""
def palavraMaisLonga(s1):
  palavras = s1.split()

  palavraLonga = max(palavras, key=len)
  return palavraLonga

#exemplo
frase = input("Digite uma frase: ")
resultado = palavraMaisLonga(frase)
print(resultado, "é a palavra mais longa da frase")