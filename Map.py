#Map Function   
    #Muito utilizado com listas
    #Função associada a um iterable
    #Aplicar uma função a um iterable, por item.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Multpicar x por 2 - Quero que o valor x seja cada item da lista x[0],[1]...
#Quero a função associada/mapeada a lista

def multi(x):
    return x * 2

#Se passar só o map(função, iterable), retornara um objeto. Precisamos passar um argumento antes(list,dict..)
lista2 = list(map(multi, lista1))
print(lista2)


entrada = input().split()
dici = {x == entrada for x in entrada}
print(dici)

print(lista2)