principal = []
auxiliar = [] #Não podemos fazer a declaracão das listas na mesma linha e por [] no final, isso iria gerar uma ligacão.
menor = maior = 0

while True:
    #inicializaão
    escolha = " " #necessário para resetar, tem que ter esse espaco tbm.

    #coleta
    auxiliar.append(input("Insira o nome: "))
    auxiliar.append(int(input("Insira a idade: ")))

    #análise maior e menor
    if len(principal) == 0:
        maior = auxiliar[1]
        menor = auxiliar[1]
    elif auxiliar[1] > maior:
        maior = auxiliar[1]
    elif auxiliar[1] < menor:
        menor = auxiliar[1]

    #anexacão
    principal.append(auxiliar[:])

    #limpar temporária
    auxiliar.clear()

    #curadoria escolha
    while escolha not in "SN":
        escolha = input("Você deseja cadastrar outros? [S/N]: ").strip().upper()
    if escolha == "N":
        break

#resultados
print("-=-"*15)
print(f"Foram cadastrados {len(principal)} pessoas.")
print("A(s) pessoa(s) mais velha(s):", end=" ")

#mostrando os maiores
for elemento in principal:
    if elemento[1] == maior: #tem que ser 1 pois 1 representa a idade
        print(elemento[0], end="; ") #0 representa o nome

#mostrando os menores
print(f"\nE a(s) pessoa(s) mais nova(s):", end=" ")
for elemento in principal:
    if elemento[1] == menor:
        print(elemento[0], end="; ")