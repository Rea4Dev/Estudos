
#! Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("Digite a distância (apenas valor em Km): "))

if dist<=200:
    print(f"O preço final sairá por {dist * 0.5}")
else:
    print(f"O preço final sairá por {dist * 0.45}")