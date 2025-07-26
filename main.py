from mapeador import gerar_simbolo, gerar_simbolos_estado,mostrar_simbolos, mapeamento
from regras_estado import *


# testes de funções

gerar_simbolos_estado(1)

# Mostrar os primeiros símbolos gerados
print("Primeiros símbolos:")
mostrar_simbolos(10)

# Você também pode acessar o dicionário diretamente:
print("Total de símbolos gerados:", len(mapeamento))