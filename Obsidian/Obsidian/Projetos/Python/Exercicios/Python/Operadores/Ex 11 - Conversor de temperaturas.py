
#! Escreva um programa que converta uma temperatura digitada em °C para °F.

temperatura = float(input("Insira a temperatura em celcius: "))
print(f"{temperatura:.0f} C° equivalem a {(temperatura * 9/5) + 32:.0f} F°.")