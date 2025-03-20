
#! Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual sua velicidade atual?: "))

if velocidade>80:
    print(f"Você foi multado. Terá que pagar R$ {(velocidade-80)*7}")
else:
    print("Tudo certo, continue assim.")