"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import date

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - anoNascimento

if idade > 25:
    print(f"Você tem {idade} anos.")
    print("Master.")
elif idade >= 19:
    print(f"Você tem {idade} anos.")
    print("Sênior.")
elif idade >= 14:
    print(f"Você tem {idade} anos.")
    print("Junior.")
elif idade >= 9:
    print(f"Você tem {idade} anos.")
    print("Infantil.")
else:
    print(f"Você tem {idade} anos.")
    print("Mirim.")