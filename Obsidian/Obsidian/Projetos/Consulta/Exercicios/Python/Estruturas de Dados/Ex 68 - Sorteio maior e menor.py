from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
tupla = sorted(tupla)
maior = tupla[0]
menor = tupla[0]
for i in range(1, len(tupla)):
    if tupla[i] > tupla[i-1]:
        maior = tupla[i]
    elif tupla[i] < tupla[i-1]:
        menor = tupla[i]
print(tupla)
print(f"O maior é {maior} e o menor é {menor}")