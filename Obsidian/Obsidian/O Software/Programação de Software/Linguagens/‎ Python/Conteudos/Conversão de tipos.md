Nesta página vamos explorar os principais métodos e cuidados sobre conversão de tipos (type conversion) em Python. A **conversão** *pode* ser feita de forma explícita com funções built-in ou de forma implícita em operações que misturam diferentes tipos. Aqui, você encontrará exemplos e dicas úteis para evitar erros comuns.
# Conversão Explícita e Implícita

Em Python, a conversão de tipos pode ocorrer de duas maneiras principais:

- ``Conversão Explícita``: quando o programador utiliza funções específicas para converter valores de um tipo para outro. Ex: int(), float(), str().

- ``Conversão Implícita``: quando o Python converte automaticamente um tipo para outro durante certas operações. Por exemplo, ao somar um inteiro com um float, o resultado é um float.


# Conversão com Funções Built-in

## int()

A função int() converte números ou strings para um inteiro. Alguns pontos importantes:

- Se o argumento for um número float, ele trunca a parte decimal.

- É possível converter uma string que representa um número inteiro; caso contrário, gera erro.


Exemplos:
```python
valor1 = int(3.9)  # resultado: 3
valor2 = int("10")  # resultado: 10
valor3 = int("10.5")  # gera ValueError
```

## float()

A função float() converte números ou strings para ponto flutuante:

```python
valor1 = float(5)       # resultado: 5.0
valor2 = float("3.14")  # resultado: 3.14
```

Lembre-se de que ao converter uma string para float, o formato deve estar correto (ponto para separar a parte decimal).

## str()

Converter outros tipos para string é feito com a função str(). Isso é útil para concatenar mensagens ou para imprimir valores.

```python
valor1 = str(100)     # resultado: "100"
valor2 = str(3.14)    # resultado: "3.14"
```

## bool()

A função bool() converte um valor para um booleano. No Python, os valores considerados “``falsy``” (que se avaliam como False) são:

- None

- False

- Números zero (0, 0.0, 0j)

- Sequências ou coleções vazias ("" , (), [], {})

Exemplo:

```python
valor1 = bool(0)      # resultado: False
valor2 = bool("oi")   # resultado: True
valor3 = bool([])     # resultado: False
```

# Conversão em Estruturas de Dados

Também é comum converter estruturas de dados. Veja alguns exemplos:

## Listas, Tuplas e Sets

- Para converter uma sequência para lista:

```python
tupla = (1, 2, 3)
lista = list(tupla)  # resultado: [1, 2, 3]
```

- Converter para tupla:

```python
lista = [1, 2, 3]
tupla = tuple(lista)  # resultado: (1, 2, 3)
```

- Converter para set (removendo duplicatas):

```python
lista = [1, 2, 2, 3]
conjunto = set(lista)  # resultado: {1, 2, 3}
```

## Dicionários

Se precisar converter coleções de pares chave-valor:

```python
lista_de_tuplas = [("a", 1), ("b", 2)]
dicionario = dict(lista_de_tuplas)  # resultado: {"a": 1, "b": 2}
```

# Função Type

Um possível aliado no tratamento de debug de tipos é a função `type()`. Utilize-a sempre que obter um tipo!
```Python
var1 = "abacate"
print(type(var1))
```

# Considerações Finais

## Cuidados e Possíveis Erros

- Certifique-se de que o valor a ser convertido esteja no formato esperado; Por exemplo, tentar converter uma string que não representa um número usando int() ou float() vai gerar um ValueError.

- Ao converter tipos complexos, como listas de strings para números, pode ser necessário iterar pela coleção:

```python
lista_str = ["1", "2", "3"]
lista_int = [int(item) for item in lista_str]
```

- Lembre-se que a conversão implícita não ocorre em todas as operações. Sempre faça a conversão explicitamente quando necessário para evitar inconsistências.

## Conversões Automáticas em Operações

Em operações aritméticas envolvendo tipos diferentes, o Python segue uma hierarquia:
inteiros podem se transformar em floats se o outro operando for um float.

Exemplo:

```python
resultado = 5 + 3.2   # resultado: 8.2 (5 é convertido para 5.0)
```

Esse comportamento é importante para entender como os dados se comportam durante cálculos e evitar surpresas.

## Dicas e Boas Práticas

- Sempre trate e valide os dados de entrada antes da conversão. Isso pode ser feito com condicionais ou tratamento de exceções (try/except).

- Documente suas conversões quando o código estiver em um projeto maior para facilitar a manutenção.

- Entenda a lógica de conversão implícita para evitar erros sutis que podem surgir em cálculos ou operações em coleções.

- Experimente no shell interativo do Python para testar diferentes conversões e observar os resultados imediatamente.