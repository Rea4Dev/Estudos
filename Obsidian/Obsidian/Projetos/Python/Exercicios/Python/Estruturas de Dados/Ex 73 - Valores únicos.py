#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
duplicados = []
while True:
    opcao = " "
    valor = int(input("Valor a ser adicionado: "))
    if lista.count(valor) == 0:
        lista.append(valor)
    else:
        duplicados.append(valor)

    while opcao not in "SN":
        opcao = input("Deseja continuar?: ").strip().upper()
    if opcao == "N":
        break

if duplicados != []:
    duplicados.sort()
    print("Valores que estavam duplicados: ", end="")
    for i in range(0, len(duplicados)):
        if duplicados.count(duplicados[i]) == 1:
            print(duplicados[i], end=" ")

lista.sort()
print(f"\nOs valores únicos e em ordem crescente são:\n{lista}")

