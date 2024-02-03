"""
Problema 3✅: Escreva um programa que inicialize três strings distintas, 
e na sequência unifique-as em uma nova variável. Sem utilizar métodos explícitos 
de remoção, na string unificada anteriormente, mantenha apenas a primeira e a última 
string inicialmente inseridas.
"""
s1 = "Esta é a primeira string."
s2 = "Esta é a segunda string."
s3 = "Esta é a terceira string."

s_concatenada = s1 + s2 + s3

# Encontra o índice inicial e final da substring s2 na s_concatenada
indice_inicial = s_concatenada.find(s2)
indice_final = indice_inicial + len(s2)

# Remove a substring s2 usando metodo de fatiamento
s_concatenada_sem_s2 = s_concatenada[:indice_inicial] + s_concatenada[indice_final:]

print(s_concatenada_sem_s2)