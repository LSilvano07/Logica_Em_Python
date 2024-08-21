#identificar quais produtos foram mais vendidos durante um dia específico

def produto_mais_vendido(produtos):
    dici = {}
    for palavra in produtos:
        if palavra in dici: 
            dici[palavra] += 1
        else: 
            dici[palavra] = 1

    produto_mais_frequente = max(dici, key=dici.get) 
    return f"{produto_mais_frequente}"       

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    lista_strings = [s.strip() for s in entrada.split(',')]
    print(lista_strings)
    return lista_strings

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))