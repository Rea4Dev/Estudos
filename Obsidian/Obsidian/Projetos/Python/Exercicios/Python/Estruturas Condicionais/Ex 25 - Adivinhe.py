
#! Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")

pcNumber = random.randint(0, 5)

playerNumber = int(input("Em que número eu pensei? "))

if pcNumber==playerNumber:
    print("Você venceu.")
else:
    print("Você perdeu.")