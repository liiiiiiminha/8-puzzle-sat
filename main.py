from solver import *
from mapeador import *
import random
import copy

# Embaralha o estado final aplicando movimentos válidos do 0
def embaralhar_estado(base, passos=10):
    def pos_zero(tab):
        for i in range(3):
            for j in range(3):
                if tab[i][j] == 0:
                    return i, j

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
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
    # Estado final padrão
    base = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    estado_inicial = embaralhar_estado(base, passos=10)

    print("🧩 Estado embaralhado:")
    for linha in estado_inicial:
        print(linha)

    modelo, passos = resolver_puzzle(estado_inicial, MAX_PASSOS=20)

    if modelo:
        estados, acoes = interpretar_modelo(modelo, mapeamento)
        estados[1] = [[str(valor) for valor in linha] for linha in estado_inicial]
        
        passos_ordenados = sorted(estados.keys())

        for idx in range(len(passos_ordenados) - 1):
            k = passos_ordenados[idx]

            print(f"\n🔹 Estado no passo {k}:")
            for linha in estados[k]:
                print(" ".join(linha))

            # ✅ Mostra a ação correta feita para gerar o estado seguinte
            if k in acoes:
                print(f"Ação realizada: {acoes[k]}")

            print(f"\n🔸 Resultado após ação (passo {k+1}):")
            for linha in estados[k+1]:
                print(" ".join(linha))
        print(" → ".join(acoes[k] for k in sorted(acoes)))

        print("\n📦 Estado final (objetivo):")
        for linha in estados[passos_ordenados[-1]]:
            print(" ".join(linha))

        print("\n🧭 Sequência de ações para resolver (desconsiderar a último):")
        print(" → ".join(acoes[k] for k in sorted(acoes)))
    else:
        print("❌ Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()