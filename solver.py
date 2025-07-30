from pysat.formula import CNF
from pysat.solvers import Solver
from collections import defaultdict
from mapeador import *
from regras_estado import *
from regras_acao import *
from regras_transicao import *

MAX_PASSOS = 20

def estado_para_clausulas(estado, p, simbolo):
    clausulas = []
    for i in range(1, 4):       # linhas 1 a 3
        for j in range(1, 4):   # colunas 1 a 3
            valor = estado[i - 1][j - 1]
            clausulas.append([simbolo(f"{p}_P_{i}_{j}_{valor}")])
    return clausulas


def estado_final(p, simbolo):
    meta = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    clausulas = []
    for i in range(1, 4):
        for j in range(1, 4):
            v = meta[i - 1][j - 1]
            clausulas.append([simbolo(f"{p}_P_{i}_{j}_{v}")])
    return clausulas

def estado_inicial(p, simbolo):
    estado = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]

    clausulas = []
    for i in range(1, 4):
        for j in range(1, 4):
            v = estado[i - 1][j - 1]
            clausulas.append([simbolo(f"{p}_P_{i}_{j}_{v}")])
    return clausulas

def resolver_puzzle(estado_inicial, MAX_PASSOS):
        
        for N in range(1, MAX_PASSOS + 1):
            cnf = CNF()

            for p in range(1, N  + 1):
                gerar_simbolos_estado(p)
                gerar_simbolos_acao(p)
                cnf.extend(regras_estado(p, simbolo))
                cnf.extend(regras_acao(p, simbolo))

                if p < N:
                    gerar_simbolos_estado(p + 1)
                    cnf.extend(regras_transicao(p, simbolo))

            # fixa o estado inicial        
            for i in range(1, 4):
                for j in range(1, 4):
                    valor = estado_inicial[i - 1][j - 1]
                    cnf.append([simbolo(f"1_P_{i}_{j}_{valor}")])
            

            cnf.extend(estado_final(N, simbolo))

            solver = Solver()
            solver.append_formula(cnf)

            if solver.solve():
                modelo = solver.get_model()
                print(f"Solução encontrada para {N} passos:")
                return modelo, N
        return None, None


def interpretar_modelo(modelo, mapeamento):
    estados = defaultdict(lambda: [[" "]*3 for _ in range(3)])
    acoes = {}

    for nome, codigo in mapeamento.items():
        if codigo in modelo:
            if "_P_" in nome:
                # Ex: "3_P_2_1_4"
                k, _, i, j, v = nome.split("_")
                estados[int(k)][int(i)-1][int(j)-1] = v

            elif "_A_" in nome:
                # Ex: "2_A_C"
                k, _, direcao = nome.split("_")
                acoes[int(k)] = direcao

    return estados, acoes

