from random import randint

jogadorNum = pcParidade = pcNum = soma = vitorias = 0
eParidade = " "

while True:
    #Entrada jogador
    while jogadorNum not in range(1, 10):
        jogadorNum = int(input("\nEscolha entre 1 a 9: "))
    while eParidade not in "pi":
        eParidade = input("Par ou ímpar [P/I]?: ").strip().lower()

    #Entrada pc
    pcNum = randint(1, 9)
    print(f"Pc escolheu: {pcNum}")
    
    #Relações
    soma = jogadorNum + pcNum
    if (soma % 2) == 0:
        if eParidade == "p":
            print("Você venceu!")
            vitorias += 1
            jogadorNum = 0
            eParidade = " "
        else:
            print("\n\nVocê perdeu.")
            break
    else:
        if eParidade == "i":
            print("Você venceu!")
            vitorias += 1
            jogadorNum = 0
            eParidade = " "
        else:
            print("\n\nVocê perdeu.")
            break

print(f"\nFim.\n{vitorias} vitorias ao total.\n")