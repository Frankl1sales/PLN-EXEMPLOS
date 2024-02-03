"""
Problema 1 ✅: Solicite ao usuário que insira uma frase. 
Seu programa deve inverter a ordem das palavras na frase e 
exibi-la de trás para frente. Por exemplo, se o usuário inserir 
"Python é divertido", o programa deve exibir "divertido é Python". 
Remova espaços extras contidos na frase, se houver
"""
s1 = input("Digite uma frase: ")
lista = s1.split() # A função split retira os espaços extras
lista = list(reversed(lista))
print(" ".join(lista))