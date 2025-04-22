# Introdução

Listas são coleções ordenadas e mutáveis, o que significa que você pode modificar seus elementos após a criação. Elas podem armazenar itens de diferentes tipos, mas geralmente são usadas para itens homogêneos.
# Criando Listas

Você pode criar listas utilizando colchetes `[]` ou a função `list()`.

**Exemplos:**
```python
# Criando uma lista com colchetes
frutas = ["maçã", "banana", "laranja"]

# Criando uma lista a partir de outra estrutura
numeros = list(range(5))  # [0, 1, 2, 3, 4]
```

# Dicas e Boas Práticas

**Mutabilidade:** Lembre-se que listas são mutáveis, o que permite modificações, mas também pode causar efeitos colaterais em funções se não for manuseada com cuidado.

**Imutabilidade:** Se precisar de uma coleção imutável, considere usar tuplas.

**Evitar Métodos Ineficientes:** Alguns métodos podem ser custosos em listas muito grandes, como o remove(), que busca o elemento pelo valor.

**Organização do Código:** Utilize list comprehensions para manter seu código mais limpo e legível, mas prefira loops convencionais quando a lógica for mais complexa.