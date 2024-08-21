#Lambda Function
    #É uma função pequena sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # codigo mais 'clean'

#EX1
#somar10 = lambda x: x+10
#print(somar10(7))

#EX2

def soma(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(soma(2))