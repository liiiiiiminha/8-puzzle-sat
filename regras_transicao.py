def regras_transicao(p, simbolo):
    clausulas = []

    direcoes = {
        "C": (-1, 0),  # cima
        "B": (1, 0),   # baixo
        "E": (0, -1),  # esquerda
        "D": (0, 1)    # direita
    }

    for i in range(1, 4):       # linhas
        for j in range(1, 4):   # colunas

            for direcao, (di, dj) in direcoes.items():
                ni, nj = i + di, j + dj  # nova posição para o 0

                cond_acao = -simbolo(f"{p}_A_{direcao}")
                cond_0 = -simbolo(f"{p}_P_{i}_{j}_0")

                # garante movimento dentro do tabuleiro
                if 1 <= ni <= 3 and 1 <= nj <= 3:
                    for v in range(1, 9):  # peça a ser trocada (não o 0)
                        cond_v = -simbolo(f"{p}_P_{ni}_{nj}_{v}")

                        # troca a pos do 0 com a pos do valor ij
                        clausulas.append([cond_acao, cond_0, cond_v, simbolo(f"{p+1}_P_{ni}_{nj}_0")])
                        clausulas.append([cond_acao, cond_0, cond_v, simbolo(f"{p+1}_P_{i}_{j}_{v}")])

                        # mantém o restante dos valores do tabuleiro
                        for x in range(1, 4):
                            for y in range(1, 4):
                                if (x, y) not in [(i, j), (ni, nj)]:
                                    for valor in range(9):
                                        clausulas.append([
                                            cond_acao,
                                            cond_0,
                                            cond_v,
                                            -simbolo(f"{p}_P_{x}_{y}_{valor}"),
                                            simbolo(f"{p+1}_P_{x}_{y}_{valor}")
                                        ])
                        for dir2 in direcoes:
                            if dir2 != direcao:
                                clausulas.append([
                                    cond_0,
                                    cond_v,
                                    cond_acao,
                                    -simbolo(f"{p}_A_{dir2}")  # nega outras ações
                                ])
                # movimento fora do tabuleiro, repetir o mesmo estado
                else:
                    for x in range(1, 4):
                        for y in range(1, 4):
                            for valor in range(9):
                                clausulas.append([
                                    cond_acao,
                                    cond_0,
                                    -simbolo(f"{p}_P_{x}_{y}_{valor}"),
                                    simbolo(f"{p+1}_P_{x}_{y}_{valor}")
                                ])
    return clausulas