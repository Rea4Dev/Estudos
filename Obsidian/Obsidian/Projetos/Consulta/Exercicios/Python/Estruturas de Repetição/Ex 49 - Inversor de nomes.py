str = input("Digite a string: ").strip().upper()
strSplit = str.split()
strJoin = "".join(strSplit)
inv = ''

for i in range(len(strJoin) - 1, -1, -1):
    inv = inv + strJoin[i]

if inv == strJoin:
    print("Palíndromo!")
else:
    print("Não é palíndromo.")