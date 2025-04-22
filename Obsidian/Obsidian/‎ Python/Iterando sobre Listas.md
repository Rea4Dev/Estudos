Percorrer uma lista é uma operação comum. Use um loop for para iterar sobre os elementos.

```Python
for fruta in frutas:
    print(f"Eu gosto de {fruta}!")

Também é possível iterar utilizando o índice, com a função enumerate():

for indice, fruta in enumerate(frutas):
    print(f"Na posição {indice} temos a fruta {fruta}")
```