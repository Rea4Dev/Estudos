tupla = (int(input("Digite um número: ")), 
         int(input("Digite um outro número: ")), 
         int(input("Digite um outro número: ")), 
         int(input("Digite um outro número: ")))

print(f"\nVocê digitou {tupla}")

for i in range(0, len(tupla)):
    if (tupla[i] % 2) == 0:
        print(f"{tupla[i]} é par.")

if 9 in tupla:
    print(f"\nO valor 9 apareceu {tupla.count(9)} vezes\n")

if 3 in tupla:
    print(f"O número 3 apareceu na {tupla.index(3) + 1} posição\n")