
#! Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = input("Digite a sua data de nascimento: ")
anos = date.today().year - int(nascimento[6:])
if anos > 18:
    print(f"Você é maior de idade. Passou {anos - 18} anos desde quando você deveria ter se alistado.")
elif anos == 18:
    print(f"É a hora de você se alistar! Você tem {anos} anos!")
else:
    print(f"Calma nenê, ainda faltam {18 - anos} anos para você se alistar!")