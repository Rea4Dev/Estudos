
#! Esceva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite em metros o valor a ser convertido para decímetros, centímetros e milímetros: "))
print(f"{metros:.1f}M ➡ {metros*10:.1f}dm ➡ {metros*100:.1f}cm ➡ {metros*1000:.1f}mm.") 