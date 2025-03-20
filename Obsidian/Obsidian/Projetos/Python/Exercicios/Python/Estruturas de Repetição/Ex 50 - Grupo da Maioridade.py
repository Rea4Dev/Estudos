
#! Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

lista = []
maiores = 0

for i in range(1, 8):
    digitado = int(input(f"Digite o {i}° elemento: "))
    lista.append(digitado) 
    if (date.today().year - digitado) >= 18:
        maiores = maiores + 1

print(f"{maiores} são maiores de idade.")
print(f"{len(lista) - maiores} são menores de idade.")