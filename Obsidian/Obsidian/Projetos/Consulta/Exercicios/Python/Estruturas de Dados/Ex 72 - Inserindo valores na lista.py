#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for i in range(0, 6):
    lista.append(int(input("Digite um valor: ")))
for i in range(0, len(lista)):
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    elif lista[i] > lista[i-1]:
        maior = lista[i]
    elif lista[i] < lista[i-1]:
        menor = lista[i]
print(f"A lista é {lista}, o maior valor é {maior} na posição {lista.index(maior) + 1} e o menor é {menor} na posição {lista.index(menor) + 1}")