#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#Declaração das variáveis
valores = []

#Entrada
for i in range(0, 7):
    valores.append(int(input(f"Digite o {i+1}° valor: ")))

#Preparação
valores.append([])
valores.append([])

#Organização paridade
for elementoPai in range(0, 7):
    if (valores[elementoPai] % 2) == 0:
        valores[8].append(valores[elementoPai])
    else:
        valores[7].append(valores[elementoPai])

#Organizando ordem
valores[-1].sort()
valores[-2].sort()

#Eliminando anteriores
for i in range(0, 7):
    del valores[0]

#Saída
print(valores)