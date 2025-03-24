tupla = ("zero", "um", "dois", "três", "quatro", "cinco")
num = int(input("Digite um número: "))

while True:
    num = int(input("Tente novamente: "))
    if 0 <= num < 6:
        break

print(f"Você digitou o número {tupla[num]}")