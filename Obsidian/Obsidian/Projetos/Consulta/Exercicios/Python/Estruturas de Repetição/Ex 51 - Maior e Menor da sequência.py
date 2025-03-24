
#! Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for pessoaAtual in range(1, 6):
    peso = float(input(f"Digite o {pessoaAtual}° peso: "))
    if pessoaAtual == 1:
        maior = peso
        menor = peso #? Se é a primeira pessoa, ela será a maior e a menor até o momento.
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior é {maior}Kg e o menor é {menor}Kg.")