listapar = []
listaimpar =[]


for i in range(11):
    numero = int(input('digite um numero: '))
    if numero % 2 ==0:
        listapar.append(numero)
    elif numero % 2 != 0:
        listaimpar.append(numero)


print (listapar, listaimpar)