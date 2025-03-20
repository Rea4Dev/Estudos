
#! Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#? Minha resolução
resultado = 0
lista = []

for i in range(1, 7):
    lista.append(int(input("Digite um valor: ")))
    if i%2==0:
        resultado = resultado + i

print(f"O resultado da soma dos pares é {resultado}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

#? Resolução Professor
soma = 0
count = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma = soma + num
        count = count + 1

print(f"Você informou {count} numeros pares e a soma foi {soma}.")