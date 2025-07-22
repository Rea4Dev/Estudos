# print()

A função print() é utilizada para exibir informações na saída padrão (geralmente o terminal ou console). Ela pode exibir diversos tipos de dados, como strings, números e variáveis. Veja alguns pontos chave:

## Parâmetros Importantes:

``sep``: define o separador entre os valores. Por padrão, é um espaço.

``end``: define o que é adicionado no final da impressão. Por padrão, é uma nova linha.

``file``: permite direcionar a saída para outro destino, como um arquivo.

``flush``: força a limpeza do buffer de saída se definido como True.

Imprime uma string simples
```python
print("Olá, mundo!")
```

Imprime múltiplos valores com separador customizado
```python
print("Olá", "Rea", sep=", ")
```

Imprime sem pular linha no final
```python
print("Linha sem quebra", end=" ")
print("continua na mesma linha")
```


---

# input()

A função input() é usada para capturar dados digitados pelo usuário. Ela pausa a execução do programa e espera o usuário inserir algo, retornando esse valor como uma string.

## Sintaxe:

```python
variavel = input("Mensagem para o usuário: ")
```

- Sempre retorna uma string. Se precisar de outro tipo de dado (ex.: inteiro ou float), é necessário converter.
- Útil para interatividade em aplicações de linha de comando.

---

# Dicas Adicionais

## Conversão de Tipos:
Lembre-se que o input() sempre retorna uma string. Use funções como int() e float() para converter a entrada para tipos numéricos.

## Customização de print():
Use os parâmetros sep e end para formatar a saída conforme a necessidade. Por exemplo, para criar uma lista separada por vírgulas:

```python
lista = [1, 2, 3, 4]
print("Números:", *lista, sep=", ")
```

## Validação de Entrada:
Em programas mais robustos, é importante validar os dados recebidos do input() para evitar erros de conversão ou entradas inválidas.
