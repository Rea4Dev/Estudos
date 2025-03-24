
#! Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Insira o valor da casa: "))
salario = float(input("Insira seu salário: "))
anosPagar = float(input("Em quantos anos pretende pagar?: "))
prestacao = (valorCasa/anosPagar)/12

if prestacao > (30/100)*salario:
    print(f"Você não pode pagar por esta casa. A prestação (R${prestacao:.2f}) excede 30 por cento de seu salário.")
else:
    print(f"Você está permitido a adquirir esta casa. A prestação (R${prestacao:.2f}) não excede 30 por cento de seu salário.")