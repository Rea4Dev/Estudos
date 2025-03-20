
#! Escreva um programa que pergunte qual a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Digite a quantidade de dias passados: "))
km = float(input("Digite a quantidade de Km rodados: "))
print(f"O valor total a se pagar é R${(km*0.15) + (dias*60)}.")