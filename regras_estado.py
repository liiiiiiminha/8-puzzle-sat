# Gerar todas as cláusulas lógicas que garantem duas regras básicas para o tabuleiro no estado p:

def regras_estado(p, simbolo):
    clausulas = []     # lista de int p/ armazenar cláusulas

    # regra 1: cada posição tem exatamente um valor
    for i in range(1, 4):
        for j in range(1, 4):               # pelo menos 1 valor
            clausula = [simbolo(f"{p}_P_{i}_{j}_{v}") for v in range(9)]
            clausulas.append(clausula)

            for v1 in range(9):             # no máximo 1 valor
                for v2 in range(v1 + 1, 9):
                    clausulas.append([-simbolo(f"{p}_P_{i}_{j}_{v1}"), -simbolo(f"{p}_P_{i}_{j}_{v2}")])

    # regra 2: cada valor aparece em exatamente uma posição
    for v in range(9):              
        simbolos = [simbolo(f"{p}_P_{i}_{j}_{v}") for i in range(1, 4) for j in range(1, 4)] # todas as posições possíveis para o valor v
        clausulas.append(simbolos)

        # no máximo 1 vez (pares)
        for idx1 in range(len(simbolos)):
            for idx2 in range(idx1 + 1, len(simbolos)):
                clausulas.append([-simbolos[idx1], -simbolos[idx2]])
    return clausulas