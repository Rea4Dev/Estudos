
#! Faça um programa que identifique se a pessoa tem em alguma parte o nome igual o seu. O programa deve ser capaz de comportar espaços indevidos e não ser case-sensitive.

nome = input("Digite seu nome: ")
print(f"Você é meu xará?: {"Renan" in nome.title()}")