
#! Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

digitado = input("Digite algo")
print(f'Você digitou "{digitado}"')

print(f"\nÉ {type(digitado)}")

print(f"\nNumérico?: {digitado.isnumeric()}")
print(f"Alfabético?: {digitado.isalpha()}")
print(f"Alfa-numérico (tipo de notação)?: {digitado.isalnum()}")
print(f"ASCII (tipo de texto)?: {digitado.isascii()}")
print(f"Decimal?: {digitado.isdecimal()}")
print(f"Digito?: {digitado.isdigit()}")
print(f"Nome permitido para variável?: {digitado.isidentifier()}")
print(f"Toda string em minúscula?: {digitado.islower()}")
print(f"Toda string em maiúscula?: {digitado.isupper()}")
print(f"Imprimível na saída?: {digitado.isprintable()}")
print(f"É inteira de espaços vazios?: {digitado.isspace()}")
print(f"É um título?: {digitado.istitle()}")