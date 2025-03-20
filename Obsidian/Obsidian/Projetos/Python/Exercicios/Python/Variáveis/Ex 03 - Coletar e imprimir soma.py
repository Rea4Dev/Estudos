
#! Crie um programa que leia dois números e mostre a soma entre eles.

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print(f"A soma entre {numero1} e {numero2} é {float(numero1)+float(numero2)}")

#----------------------------------------------------------------------------------------------#

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print('A soma entre {} e {} é {}'.format(numero1, numero2, float(numero1)+float(numero2)))

#----------------------------------------------------------------------------------------------#

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print("A soma entre",  numero1, "e", numero2, "é", float(numero1)+float(numero2))