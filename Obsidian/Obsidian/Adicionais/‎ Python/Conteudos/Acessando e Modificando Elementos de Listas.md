Cada elemento na lista tem um índice, começando de 0. Você pode acessar, atualizar ou remover elementos pela sua posição.

``Exemplos:``
``` Python
frutas = ["maçã", "banana", "laranja"]

# Acessando o primeiro elemento
print(frutas[0])  # saída: maçã

# Modificando o segundo elemento
frutas[1] = "morango"
print(frutas)  # saída: ['maçã', 'morango', 'laranja']

# Acessando elementos com índices negativos
print(frutas[-1])  # saída: laranja
```

Você também pode utilizar slicing para acessar sublistas:
```Python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0:2])  # saída: ['maçã', 'banana']
```