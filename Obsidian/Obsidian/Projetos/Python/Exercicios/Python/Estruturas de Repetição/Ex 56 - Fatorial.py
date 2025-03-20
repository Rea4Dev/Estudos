# Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input("Insira um número: "))
anterior = num - 1
while anterior != 1:
    num = num * anterior
    anterior = anterior - 1
print(f"O fatorial é = {num}")