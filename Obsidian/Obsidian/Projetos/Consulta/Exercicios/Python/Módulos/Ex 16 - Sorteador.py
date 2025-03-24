
#! Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nomedo escolhido.

import random

aluno1 = input("Digite o aluno 1: ")
aluno2 = input("Digite o aluno 2: ")

lista = [aluno1, aluno2] #calma, ainda veremos listas

print(f"O escolhido foi {random.choice(lista)}")

# também poderia ser feito como está abaixo
#? lista = [input("Digite o aluno 1: "), input("Digite o aluno 2: ")]