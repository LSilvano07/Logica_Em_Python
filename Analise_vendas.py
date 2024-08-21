#calcular o total de vendas e a média mensal
#criar uma lista em Python para calcular o total de vendas e a sua média mensal.    

def analise_vendas(vendas):
    total_vendas = 0
    for i in vendas:
        total_vendas += i
    media_vendas = total_vendas / len(vendas)    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    vendas_mensal_texto = input().split()
    vendas_inteiro = list(map(lambda x: int(x.replace(',', '')), vendas_mensal_texto))
    return vendas_inteiro

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))