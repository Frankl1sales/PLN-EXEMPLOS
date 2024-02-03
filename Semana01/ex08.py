"""
Problema 8 ✅: Uso de Expressões Regulares: Use expressões 
regulares para encontrar todas as ocorrências das palavras "João" e 
"Maria", inclusive como subpalavras, na história e destaque essas palavras 
no texto, reescrevendo-as com todas as letras maiúsculas.
"""
import re

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

novo_texto = re.sub(r'Maria', 'MARIA', texto)
novo_texto = re.sub(r'João', 'JOÃO', novo_texto)
print(novo_texto)