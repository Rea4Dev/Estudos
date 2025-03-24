#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 000, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = 0

while True:
    num = int(input("Digite um número: "))
    if num == 000:
        break
    else:
        cont = cont + 1
        soma = soma + num

print(f"\nLevou {cont} iterações e a soma deles é {soma}.")