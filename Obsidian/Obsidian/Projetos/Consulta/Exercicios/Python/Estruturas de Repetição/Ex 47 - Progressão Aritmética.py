
#! Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

razao = float(input("Digite a razão da P.A: "))
q1 = int(input("Digite o primeiro termo: "))
qAnterior = 0
for i in range(q1, 11):
    print(f"{qAnterior + razao:.0f}", end=" ➡  ")
    qAnterior = qAnterior + razao
print("Fim.")