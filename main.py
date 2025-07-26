from mapeador import simbolo, gerar_simbolos_estado,mostrar_simbolos, mapeamento
from regras_estado import regras_estado


# testes de funções

gerar_simbolos_estado(1)
clausulas = regras_estado(1, simbolo)

print("Total de cláusulas geradas:", len(clausulas))

# Mostrar as 5 primeiras cláusulas
for i, c in enumerate(clausulas[:5]):
    print(f"Cláusula {i+1}: {c}")

valores_invalidos = []
for clausula in clausulas:
    for literal in clausula:
        var_id = abs(literal)
        if var_id not in mapeamento.values():
            valores_invalidos.append(var_id)
