
#! Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

resultado = 0

for i in range(1, 501, 2): #começa em 1 e vai adicionando 2, garantindo sempre ser ímpar.
    if i % 3 == 0: #garantindo ser múltiplo de 3
        resultado = resultado + i #somando
print(resultado)