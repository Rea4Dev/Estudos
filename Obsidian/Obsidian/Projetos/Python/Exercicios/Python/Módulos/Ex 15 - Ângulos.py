
#! Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input("Insira o ângulo: "))

print(f"Seno: {sin(radians(angulo)):.2f}\nCosseno: {cos(radians(angulo)):.2f}\nTangente: {tan(radians(angulo)):.2f}")