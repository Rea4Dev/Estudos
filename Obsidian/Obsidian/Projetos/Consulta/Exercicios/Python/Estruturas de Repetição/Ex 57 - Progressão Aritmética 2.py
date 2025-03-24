# Leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro número: "))
razao = int(input("Digite a razão: "))
contador = 0
while contador < 10:
    contador += 1
    termo = termo + razao
    print(termo)