
#! Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Insira a largura da parede (em metros): "))
altura = float(input("Insira a altura da parede (em metros): "))
print(f"A área é {largura * altura:.0f}m². A quantidade de tinta necessária é {(largura * altura)/2:.0f} litros.")