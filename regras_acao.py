def regras_acao(p, simbolo):
    clausulas = []     

    direcoes = ["C", "B", "E", "D"]                     # Cima, Baixo, Esquerda, Direita
    acoes = [simbolo(f"{p}_A_{d}") for d in direcoes]
    clausulas.append(acoes) 

    for i in range(len(acoes)):
        for j in range(i + 1, len(acoes)):
            clausulas.append([-acoes[i], -acoes[j]])

    return clausulas