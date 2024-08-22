#MAP e Lamda - Economizar linha de código, código mais limpo e veloz

lista1 = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]

#def multi(x):
    #return x * 2
#lista2 = list(map(multi, lista1))  ---- TUDO EM UMA LINHA SÓ
#print(lista2)


lista2 = [i*2 for i in lista1]
print(lista2)


multiplicar = int(input())
lista_multiplicação = [i * multiplicar for i in range(1, 11)]
print(lista_multiplicação)
