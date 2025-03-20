# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#? -------------------------------------------------------------- Minha Versão ------------------------------------------------------------------------------#
from random import randint

escolhaPc = randint(0, 10)
escolhaUser = int(input("Tente adivinha o número que o pc pensou: "))
tentativas = 0

if escolhaPc == escolhaUser:
    print("Parabéns! Você venceu de primeira.")
else:
    while escolhaPc != escolhaUser:
        tentativas = tentativas + 1
        escolhaUser = int(input(f"{tentativas}° tentativa. Você errou, tente novamente: "))
    print(f"Você finalmente acertou na sua {tentativas}° tentativa")

#! -------------------------------------------------------------- Versão Prof ------------------------------------------------------------------------------#
from random import randint

escolhaPc = randint(0, 10)
print(escolhaPc)
acertou = False
tentativas = 0

while not acertou:
    escolhaUser = int(input("\n\nTente adivinhar o número que o pc pensou: "))
    tentativas = tentativas + 1
    if escolhaUser == escolhaPc:
        acertou = True
    else:
        if escolhaUser < escolhaPc:
            print("É maior que isso...")
        if escolhaUser > escolhaPc:
            print("É menor que isso...")

print(f"Você finalmente acertou na sua {tentativas}° tentativa")