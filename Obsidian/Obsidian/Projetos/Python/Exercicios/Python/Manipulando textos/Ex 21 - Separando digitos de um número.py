
#? Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

#---------------------------------------------------------------------------------------------------------------------------------------------#
#! Mão funciona se menor que 4 dígitos
num = input("Digite o número até 9999: ")
numSplited = num.split()

print(f"O número digitado foi: {num}.\nMilhar: {numSplited[0][0]}\nCentena: {numSplited[0][1]}\nDezena: {numSplited[0][2]}\nUnidade: {numSplited[0][3]}")
#---------------------------------------------------------------------------------------------------------------------------------------------#
#! Mão funciona se menor que 4 dígitos
num = input("Digite o número até 9999: ")
numStringed = str(num)

print(f"O número digitado foi: {num}.\nMilhar: {numStringed[0]}\nCentena: {numStringed[1]}\nDezena: {numStringed[2]}\nUnidade: {numStringed[3]}")
#---------------------------------------------------------------------------------------------------------------------------------------------#

#? Melhor forma
num = int(input("Digite o número até 9999: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f"O número digitado foi: {num}.\nMilhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {unidade}")