
#! Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
numero = float(input("Digite um número decimal: "))
print(f"A parte inteira do número é {trunc(numero)}")
print(f"A parte inteira do {numero} é {int(numero)}") #? coloquei só por curiosidade; forma mais recomendada pois não necessita importar módulo.

# ps, não é recomendado por atrapalhar legibilidade, clareza e depuração (achar erros), mas é possível fazer a linha 2 e 3 em apenas uma, como abaixo:
# print(f"A parte inteira do número é {trunc(float(input("Digite um número decimal: ")))}")