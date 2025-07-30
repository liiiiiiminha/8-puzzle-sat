def regras_transicao(p, simbolo):
    clausulas = []

    direcoes = {
        "C": (-1, 0),  # Cima
        "B": (1, 0),   # Baixo
        "E": (0, -1),  # Esquerda
        "D": (0, 1)    # Direita
    }

    for i in range(1, 4):       # linhas
        for j in range(1, 4):   # colunas

            for direcao, (di, dj) in direcoes.items():
                ni, nj = i + di, j + dj  # nova posição para o 0

                cond_acao = -simbolo(f"{p}_A_{direcao}")
                cond_0 = -simbolo(f"{p}_P_{i}_{j}_0")

                # AÇÃO VÁLIDA — movimento dentro do tabuleiro
                if 1 <= ni <= 3 and 1 <= nj <= 3:
                    for v in range(1, 9):  # peça a ser trocada (não o 0)
                        cond_v = -simbolo(f"{p}_P_{ni}_{nj}_{v}")

                        # Troca: 0 vai para (ni, nj), v vem para (i, j)
                        clausulas.append([cond_acao, cond_0, cond_v, simbolo(f"{p+1}_P_{ni}_{nj}_0")])
                        clausulas.append([cond_acao, cond_0, cond_v, simbolo(f"{p+1}_P_{i}_{j}_{v}")])

                        # PRESERVAR o restante do tabuleiro
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
                # AÇÃO INVÁLIDA — movimento fora do tabuleiro
                else:
                    # Se tentar executar uma ação inválida, repetir TODO o estado
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