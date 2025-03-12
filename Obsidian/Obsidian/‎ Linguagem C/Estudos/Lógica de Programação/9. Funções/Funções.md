As funções são blocos de código reutilizáveis que realizam tarefas específicas e podem ser chamadas de diferentes partes de um programa. Elas promovem modularidade, facilitam a manutenção e a legibilidade do código. Cada função em C tem a seguinte estrutura básica:

```C
tipo_de_retorno nome_da_funcao(tipo1 param1, tipo2 param2, ...) {
    // Corpo da função
    return valor; // Opcional, dependendo do tipo de retorno
}

```
> Em C não se pode definir funções dentro de funções.

>[!NOTE] Sempre que no cabeçalho de uma função não é colocado o tipo de retorno, este é substituído pelo tipo int.

``Veja que``: Podemos usar do valor de uma função como argumento de outra função
```C
printf("%d %d", dobro(5), soma(dobro(2),3+2));

ou

if (soma(x,y) > 0 )
```
## Elementos de uma Função
-  [[Parâmetros]]
-  [[Retorno]]
-  [[Protótipo de Função]]
- [[Passagem de Vetores para Funções]]