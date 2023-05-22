nome = []
idade = []

menor = []

for i in range (10):
    name = input('Digite o nome: ')
    nome.append(name)
    age = int(input('Digite a idade (numero inteiro apenas): '))
    idade.append(age)

for i in range(len(nome)):
    if idade[i] < 18:
        menoridade = nome[i]
        menor.append(menoridade)
print(menor)
