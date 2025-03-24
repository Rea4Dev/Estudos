
#! Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorOriginal = float(input("Insira o valor original do produto: "))
print(f"O valor inserido foi R${valorOriginal:.0f}, sendo este o valor original.\nO valor agora com desconto é R${valorOriginal - (5/100 * valorOriginal):.0f}")