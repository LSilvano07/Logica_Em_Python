#MAP e Lamda - Economizar linha de código, código mais limpo e veloz

lista1 = [1, 2, 3, 4]

#def multi(x):
    #return x * 2
#lista2 = list(map(multi, lista1))  ---- TUDO EM UMA LINHA SÓ
#print(lista2)

lista2 = list(map(lambda x: x * 2, lista1))
print(lista2)

#FILTER