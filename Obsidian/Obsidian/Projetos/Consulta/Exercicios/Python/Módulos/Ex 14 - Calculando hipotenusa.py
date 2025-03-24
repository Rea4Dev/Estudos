
#! Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

catetoOposto = float(input("Insira o cateto oposto: "))
catetoAdjacente = float(input("Insira o cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f"O valor da hipotenusa é: {hipotenusa:.2f}")
print(f"O valor da hipotenusa é: {(  (catetoAdjacente**2 + catetoOposto**2) ** (1/2)  ):.2f}") #? Forma alternativa sem precisar de módulo.