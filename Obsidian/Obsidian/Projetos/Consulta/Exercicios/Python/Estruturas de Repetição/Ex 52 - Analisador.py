
#! Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdade = 0
idade = 0
media = 0
nome_h_velho = ""
idade_h_velho = 0
total_mulher_sub20 = 0

for i in range(1, 5):

    print(f"---- {i}° Pessoa ----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    somaIdade = somaIdade + idade

    if i == 1 and sexo in "M": #poderia ser "Mm" e tirar o .upper() da linha 10
        idade_h_velho = idade
        nome_h_velho = nome
    if idade > idade_h_velho and sexo in "M":
        idade_h_velho = idade
        nome_h_velho = nome
    if idade < 20 and sexo in "F":
        total_mulher_sub20 = total_mulher_sub20 + 1

media = somaIdade / 4

print(f"\nA média da idade do grupo é {media}")
print(f"O homem mais velho tem {idade_h_velho} e seu nome é {nome_h_velho}.")
print(f"Ao todo são {total_mulher_sub20} mulheres com menos de 20 anos.\n")