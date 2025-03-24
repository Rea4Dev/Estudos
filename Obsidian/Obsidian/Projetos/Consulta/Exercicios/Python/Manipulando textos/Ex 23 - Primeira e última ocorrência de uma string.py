
#! Faça um programa que leia uma frase pelo teclado e mostre quantas vezes apareceu a letra "A", em que posição ela aparece a primeira e a última vez.

nome = input('Digite o nome: ').lower().strip()

print(f'A letra A aparece {nome.count('a')} vezes na frase.')
print(f'A primeira letra A apareceu na posição de índice: {nome.lower().find('a')}')
print(f'A última letra A apareceu na posição de índice: {nome.lower().rfind('a')}')