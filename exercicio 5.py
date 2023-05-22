import random
import math
lista = []
numero = 3
contador = 0

for i in range(10):
    numeronovo = round(random.randint(1,10))
    lista.append(numeronovo)
print(lista)

def funcao (lista, numero):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            contador += 1
    print (contador)
funcao(lista, numero)