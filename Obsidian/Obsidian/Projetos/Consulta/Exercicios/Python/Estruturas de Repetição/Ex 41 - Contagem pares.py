
#! Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for numero in range(1, 51):
    if numero%2==0:
        print(numero)

for numero in range(2, 51, 2): #? Forma mais recomendada em processamento. Utiliza menos recurso.
    print(numero)