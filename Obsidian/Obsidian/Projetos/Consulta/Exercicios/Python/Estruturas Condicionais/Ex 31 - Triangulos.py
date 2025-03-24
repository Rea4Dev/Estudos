
#! Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

t1 = float(input("Digite o primeiro triângulo: "))
t2 = float(input("Digite o segundo triângulo: "))
t3 = float(input("Digite o terceiro triângulo: "))

if t1<(t2+t3) and t2<(t1+t3) and t3<(t2+t1):
    print("Forma um triângulo")
else:
    print("Não forma.")