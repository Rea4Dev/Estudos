"""
Refaça o desafio dos triângulos (um lado não pode ser maior que a soma dos outros dois), acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

triangulos = [float(input("Insira o primeiro: ")), float(input("Insira o segundo: ")), float(input("Insira o terceiro: "))]

if (triangulos[0]<triangulos[1]+triangulos[2]) and (triangulos[1]<triangulos[2]+triangulos[0]) and (triangulos[2]<triangulos[1]+triangulos[0]):
    print("Este triângulo existe.")
    if (triangulos[0]==triangulos[1] or triangulos[1]==triangulos[2] or triangulos[0]==triangulos[2]):
        print("Isosceles.")
    elif triangulos[0]==triangulos[1]==triangulos[2]:
        print("Equilatero")
    else:
        print("Escaleno.")
else:
    print("Este triângulo é impossível.")