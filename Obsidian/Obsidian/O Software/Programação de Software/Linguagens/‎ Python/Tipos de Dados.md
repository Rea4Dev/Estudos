---
data_criacao: 04-08-2025
flashcards: Não feito
revisão: Não feita
---
# Tipos de Dados em Python

A linguagem **Python** suporta diversos tipos de dados. Entre os tipos mais básicos e fundamentais, temos:

- `int` — números inteiros (ex: 3)
    
- `float` — números de ponto flutuante (ex: 3.0)
    
- `bool` — valores booleanos (True ou False)
    
- `str` — cadeias de caracteres (ex: 'Hello World')
    
- `list` — listas ordenadas e mutáveis (ex: \[1, 1, 2, 3, 5, 8] )
    
- `tuple` — sequências ordenadas e _imutáveis_ de elementos (ex: (1, 2, 3))
    
- `dict` — coleções de pares chave-valor (ex: {'nome': 'Rea', 'idade': 20})
    

# Objetos em Python

Em Python, **todos os dados são tratados como objetos**. Isso significa que:

> Um objeto é uma _entidade na memória_ que possui um **tipo** e um **valor**.

Esse conceito é fundamental para entender como a linguagem lida com dados, pois mesmo valores simples como números ou _strings_ são, internamente, objetos com métodos e atributos.

## Exemplos ilustrativos

```python
type(3)                      # int
type(3.0)                    # float
type('Hello')                # str
type([1, 2, 3])              # list
type((1, 2))                 # tuple
type({'a': 1, 'b': 2})       # dict
```

> Fonte: Perkovic, 2015

# Função `type()`

A função `type()` pode ser usada para verificar o tipo de um objeto em tempo de execução. Veja alguns exemplos:

```python
type(3)
# <class 'int'>

type('Olá')
# <class 'str'>

type([1, 2, 3])
# <class 'list'>
```

> [!Importante]  
> Variáveis em Python **não possuem um tipo fixo**.  
> Elas simplesmente **apontam temporariamente para um objeto na memória**.  
> Isso significa que o tipo está associado ao **objeto**, não à variável.
