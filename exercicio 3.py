import random
import math



lista = []
soma = 0
contador = 0
menor = float("inf")
maior = -float("inf")
whil = 0
while whil != 20:
    numero = round((random.random()*100) , 0)
    
    if numero <= 50:
        lista.append(numero)
        whil += 1

print(lista)
for i in range(len(lista)):
    lista[i]
    soma += lista[i]
    contador +=1

print (soma)

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
print(menor)

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
print(maior)