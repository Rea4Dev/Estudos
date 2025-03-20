#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#? -------------------------------------------------------------- Minha Versão ------------------------------------------------------------------------------#
sexo = input("Digite o sexo [M/F]: ").upper().strip()[0]

while (sexo != "M") and (sexo != "F"):
    sexo = input("\nValor não aceito.\nDigite [M/F]: ").upper().strip()

print(f"Sexo {sexo} registrado com sucesso.")


#! -------------------------------------------------------------- Versão Prof ------------------------------------------------------------------------------#
sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("\nValor não aceito.\nDigite [M/F]: ")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso.")
