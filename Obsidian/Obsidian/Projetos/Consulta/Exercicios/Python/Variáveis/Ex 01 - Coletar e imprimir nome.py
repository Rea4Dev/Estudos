
#! Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.


#? Forma 01

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")




#? Forma 02

print("Digite seu nome: ")
nome = input()
print(f"Olá, {nome}!")




#? Forma 03

print("Digite seu nome: ")
nome = input()
print("Olá, " + nome + "!")



#? Forma 04

print("Digite seu nome: ")
nome = input()
print("Olá, ", end="")
print(nome, end="")
print("!")

#Para que o print() não quebre linha após ser usado, é necessário usar este end="". Ele finalizará a linha apenas com o que tem escrito no "", que no caso, é nada.