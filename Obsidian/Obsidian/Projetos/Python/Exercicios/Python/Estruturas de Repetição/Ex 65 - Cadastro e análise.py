#Variáveis
continuar = subMulher = maiores = idade = homens = 0
sexo = " "

#Loop
while True:

    #Resetando cadastro
    sexo = " "
    idade = 0

    #Cadastro
    print("-"*20)
    print("Cadaste uma pessoa.")
    print("-"*20)
    while idade not in range(1, 101):
        idade = int(input("Digite a idade: "))
    while sexo not in "MF":
        sexo = input("Digite o sexo [M/F]: ").strip().upper()

    #Análise
    if idade > 18: #pessoas de maior
        maiores += 1
    if sexo == "M": #total de homens
        homens += 1
    else: #mulheres
        if idade < 20: #total de mulheres abaixo de 20
            subMulher += 1

    #Continuar?
    continuar = input("Desja continuar [S/N]?: ").strip().upper()
    if continuar == "N":
        break

#Saída
print(f"""
    Ao total, temos {maiores} maiores de idade.
    Temos {homens} homens.
    E temos {subMulher} mulheres abaixo de 20 anos.\n""")