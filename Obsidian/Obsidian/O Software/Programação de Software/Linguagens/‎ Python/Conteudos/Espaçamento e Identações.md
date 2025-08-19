[[Índice Python|Voltar]]

## Nível de Identação

Use **4 espaços** por nível de indentação.

## Linhas de Continuação

Pelo tamanho recomendado de linhas de códigos <small>(79)</small> e strings <small>(72)</small>, por vezes podemos necessitar, gerar linhas de continuação. Há diferentes formas de utilizá-las. Veja abaixo:

> [!TIP] Opção 01
> - As linhas de continuação devem alinhar os elementos encapsulados verticalmente usando a junção de linha implícita do Python dentro de parênteses, colchetes e chaves.
> 
> 
> ```Python
> # Alinhado com abertura de delimitador
> foo = long_function_name(var_one, var_two,
>                          var_three, var_four)
> ```

> [!TIP] Opção 2 e 3 - Recuo Deslocado
> - Ao usar um recuo deslocado, o seguinte deve ser considerado: não deve haver argumentos na primeira linha e um recuo adicional deve ser usado para se distinguir claramente como uma linha de continuação:
> 
> 
> ```Python
> # Adicionado um nível extra de itendação para distinguir argumentos dos comandos do corpo de laço
> def long_function_name(
>         var_one, var_two, var_three,
>         var_four):
>     print(var_one)
> ```
> 
> 
> ```Python
> # Recuos Deslocado com adicionar um level.
> foo = long_function_name(
>     var_one, var_two,
>     var_three, var_four)
> ```



- Não misture tabulações com espaços.
- Espaços ao redor de operadores (`=`, `+`, `*`, etc.).
- Evite múltiplos espaços em branco ou linhas vazias extras.
- Uma linha em branco entre funções e classes.
- Separe métodos dentro de classes com uma linha em branco.
- Duas linhas em branco entre seções lógicas em arquivos.
- Evite espaços:
    - Imediatamente dentro de parênteses, colchetes ou chaves.
    - Antes de `(`, `[`, ou após `]`, `)`, `}`.
- Use um espaço após vírgulas e dois pontos.

```python
# Correto
resultado = (5 * 3) + 2
lista = [1, 2, 3]

# Errado
resultado=5*3+2  # sem espaços
lista = [ 1 , 2 , 3 ]  # espaços inconsistentes
```

```Python
lista = [x * 2 for x in range(10) if x % 2 == 0]
```
