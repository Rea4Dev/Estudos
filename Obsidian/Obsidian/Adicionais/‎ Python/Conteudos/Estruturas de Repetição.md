# Introdução

Em Python, as estruturas de repetição são fundamentais para a execução de tarefas que precisam ser repetidas diversas vezes sem a necessidade de escrever o mesmo código repetidamente. As duas principais estruturas de repetição são o `while` e o `for`.

---

# While

## Sintaxe e Funcionamento

A estrutura `while` executa um bloco de código enquanto uma condição for verdadeira. Assim que a condição se tornar falsa, o loop é interrompido.

**Sintaxe:**
```python
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
```

Explicação: Neste exemplo, o loop while continua enquanto o valor de contador for menor ou igual a 5. A cada iteração, o contador é incrementado até que a condição se torne falsa.

---

# For

## Sintaxe e Funcionamento

A estrutura for em Python permite iterar sobre uma sequência (como *listas, tuplas, strings ou intervalos*). 
Ela é bastante útil ``quando se sabe o número de iterações`` ou se está trabalhando com uma ``coleção de itens``.

Explicação: Aqui, o loop for percorre cada elemento da lista numeros e imprime seu valor.
```python
numeros = [1, 2, 3, 4, 5]
for indice in numeros:
    print(f"Número: {indice}")
```


Além disso, é comum usar a função range() para criar uma sequência de números:
```python
for i in range(1, 6):
    print(f"i: {i}")
```

---

# List Comprehensions

Embora não seja uma estrutura de repetição tradicional, as list comprehensions permitem criar listas de forma concisa e "pythônica" através da iteração.

```Python
quadrados = [x**2 for x in range(10)]
print(quadrados)
```

Explicação: O código acima gera uma lista de quadrados dos números de 0 a 9.

---

# Dicas e Boas Práticas

**Legibilidade:** 
	Prefira usar for quando iterar sobre elementos de uma sequência. Isso aumenta a clareza do código.

**Utilize list comprehensions:**
	Elas podem simplificar o código quando se deseja criar novas listas a partir de uma iteração.
