from mapeador import simbolo, gerar_simbolos_estado, mapeamento, gerar_simbolos_acao
from regras_estado import regras_estado
from regras_acao import regras_acao
from solver import *
import random, copy

def embaralhar_estado(base, passos=20):
    def pos_zero(tab):
        for i in range(3):
            for j in range(3):
                if tab[i][j] == 0:
                    return i, j

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    estado = copy.deepcopy(base)

    for _ in range(passos):
        i, j = pos_zero(estado)
        random.shuffle(direcoes)
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                estado[i][j], estado[ni][nj] = estado[ni][nj], estado[i][j]
                break
    return estado

def main():
    base = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    inicial = embaralhar_estado(base, passos=10)

    print("🧩 Estado embaralhado:")
    for linha in inicial:
        print(linha)

    modelo, passos = resolver_puzzle(inicial, MAX_PASSOS=20)

    if modelo:
        from mapeador import mapeamento
        estados, acoes = interpretar_modelo(modelo, mapeamento)

passos_ordenados = sorted(estados)

for idx in range(len(passos_ordenados) - 1):
        k = passos_ordenados[idx]

        print(f"\n🔹 Estado no passo {k}:")
        for linha in estados[k]:
            print(" ".join(linha))

        if k in acoes:
            print(f"Ação realizada: {acoes[k]}")

        print(f"\n🔸 Resultado após ação (passo {k+1}):")
        for linha in estados[k + 1]:
            print(" ".join(linha))


        print("\n🔁 Sequência de ações:")
        print(" → ".join(acoes[p] for p in sorted(acoes)))
    else:
        print("❌ Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()