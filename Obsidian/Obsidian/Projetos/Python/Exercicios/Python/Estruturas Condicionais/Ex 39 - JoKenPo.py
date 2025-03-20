
#! Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

escolhaUser = int(input("""
Escolha (1) para pedra.
Escolha (2) para papel.
Escolha (3) para tesoura.
"""))
escolhaPc = randint(1, 3)

if escolhaPc == 1:
    if escolhaUser == 2:
        print(f"Pc escolheu pedra.")
        print("Você ganhou.")
    elif escolhaUser == 1:
        print(f"Pc escolheu pedra.")
        print("Empate.")
    elif escolhaUser == 3:
        print(f"Pc escolheu pedra.")
        print("Você perdeu.")
    else:
        print("Opção Inválida.")

if escolhaPc == 2:
    if escolhaUser == 3:
        print(f"Pc escolheu papel.")
        print("Você ganhou.")
    elif escolhaUser == 2:
        print(f"Pc escolheu papel.")
        print("Empate.")
    elif escolhaUser == 1:
        print(f"Pc escolheu papel.")
        print("Você perdeu.")
    else:
        print("Opção Inválida.")

if escolhaPc == 3:
    if escolhaUser == 1:
        print(f"Pc escolheu tesoura.")
        print("Você ganhou.")
    elif escolhaUser == 3:
        print(f"Pc escolheu tesoura.")
        print("Empate.")
    elif escolhaUser == 2:
        print(f"Pc escolheu tesoura.")
        print("Você perdeu.")
    else:
        print("Opção Inválida.")