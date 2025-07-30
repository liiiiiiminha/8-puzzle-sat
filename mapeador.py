#Dicionário para mapeamento de variáveis para números inteiros

mapeamento = {}
contador = 1

def simbolo(nome):
    global contador
    if nome not in mapeamento:
        mapeamento[nome] = contador 
        contador += 1
    return mapeamento[nome]

def gerar_simbolos_estado(p):
    for linha in range(1, 4):
        for coluna in range(1, 4):
            for valor in range(9):
                nome = f"{p}_P_{linha}_{coluna}_{valor}"
                simbolo(nome)

def gerar_simbolos_acao(p):
    for direcao in ["C", "B", "E", "D"]:
        nome = f"{p}_A_{direcao}"
        simbolo(nome)

def mostrar_simbolos(n):
    print(f"Símbolos gerados para o estado {n}:")
    for nome, codigo in list(mapeamento.items())[:83]:  # Mostra os 10 primeiros
        print(f"{nome} → {codigo}")