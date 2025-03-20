
#! O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

lista = [input("Aluno 1: "), input("Aluno 2: "), input("Aluno 3: "), input("Aluno 4: ")]

random.shuffle(lista)

print(f"O ordem de apresentação será:\n {lista}")