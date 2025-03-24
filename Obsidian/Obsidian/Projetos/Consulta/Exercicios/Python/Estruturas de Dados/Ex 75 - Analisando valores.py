"""
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:

    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    valor = int(input('Digite o valor: '))
    if valor == 0:
        break;
    lista.append(valor)
print(f'A quantidade de números foi {len(lista)}')
lista.sort(reverse=True)
print(f'Decrescente, fica: {lista}')
if 5 in lista:
    print("5 está na lista")
else:
    print("5 não está na lista.")