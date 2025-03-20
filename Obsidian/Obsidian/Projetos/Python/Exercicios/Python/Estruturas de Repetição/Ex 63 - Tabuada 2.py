num = 0

while True:
    num = int(input("Digite o valor para a tabuada: "))
    if num == 0:
        break
    else:
        for i in range(1, 11):
            print(f"{num} x {i:2} = {num * i}")

print("\nFim.")