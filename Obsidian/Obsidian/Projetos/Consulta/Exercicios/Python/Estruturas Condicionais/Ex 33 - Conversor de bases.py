
#! Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

escolha = int(input("""Bem vindo!
Selecione a opção (1) para converter de decimal para binário.
Selecione a opção (2) para converter de decimal para hexadecimal.
Selecione a opção (3) para converter de decimal para octal.
"""))
print("Opção escolhida.")
valor = int(input("\nDigite então o valor a ser convertido: "))
if escolha==1:
    valor = bin(valor)
elif escolha==2:
    valor = hex(valor)
elif escolha==3:
    valor = oct(valor)
else:
    print("Opção inválida.")
print(f"O valor convertido ficou {valor[2:]}.")