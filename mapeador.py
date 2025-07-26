#Dicionário para mapeamento de variáveis para números inteiros

mapeamento = {}
contador = 1

def gerar_simbolo(nome):
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
                gerar_simbolo(nome)

def mostrar_simbolos(n):
    print("Símbolos gerados para o estado 1:")
    for nome, codigo in list(mapeamento.items())[:83]:  # Mostra os 10 primeiros
        print(f"{nome} → {codigo}")