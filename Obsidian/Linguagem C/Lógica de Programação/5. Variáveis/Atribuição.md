Sempre que uma variável é **declarada**, estamos **solicitando** ao **compilador** para **reservar espaço em memória para armazená-la**. Esse espaço passará a ser **referenciado através do nome** da variável.

No caso do inteiro, o **espaço** em bytes que lhe é reservado **varia com as arquiteturas em que é utilizado**. Em microcomputadores o seu valor é normalmente de 2 bytes, enquanto em máquinas maiores é habitualmente de 4 bytes.

Independentemente do número de bytes que ocupe, o nome da variável referencia a totalidade do espaço ocupado pela variável.

Sempre que uma variável é **definida, um conjunto de bytes fica associado a ela**. Ora, esses bytes têm bits com valor 1 e outros bits com 0, constituindo um número qualquer. Dessa forma, quando uma variável é criada fica automaticamente com um valor que não é 0 nem 1, nem qualquer valor predefinido, mas sim um **valor qualquer aleatório que resulta da disposição dos bits** que se encontram nos bytes reservados para a representação dessa variável.

![[Pasted image 20241020135214.png]]

Ao realizar uma atribuição o valor anterior presente na variável é eliminado, ficando nela o novo valor que lhe foi atribuído. A atribuição de um valor só pode ser realizada para variáveis.

Uma atribuição é realizada obedecendo à seguinte sintaxe:
```
tipo nome = expressão;
```

Exemplo:
```
int num = -17;

int num2;

int n1 = 3, n2 = 5;

int a = 10, b, c = -123, d;
```

Assim como as múltiplas declarações, podemos fazer múltiplas atribuições.

A atribuição de valores em C é realizada através do sinal de **=** , chamado de **sinal de** **atribuição** e lê-se “recebe” ou “tem atribuído” (jamais chame de “igual” ou “igualdade”, pois poderá se confundir. Este símbolo é de atribuição, ele atribui algo a algo, não tem relação nenhuma com igualdade!).

## Ordem de Execução de Múltiplas Atribuições
Observe a seguinte questão:

A = 1;

B = 2;

C = 3;

D = 4;

Qual é o valor das variáveis se, em seguida, fosse executada a seguinte instrução:

A = B = C = D = 5;

A resposta é simples, todas ficam com o valor 5. A razão tem muito a ver com as características da linguagem C. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.

![[Pasted image 20241020135419.png]]

![[Pasted image 20241020135425.png]]

---
# Revisão
#flashcards/Logica_de_programação

O que acontece quando declaramos uma variável;;Indicamos ao compilador para reservar um espaço na memória.
<!--SR:!2024-10-29,4,270-->

Qual o tamanho em bytes de um int;;Na verdade, depende da arquitetura. Em microcontroladores, costuma ser 2 bytes - já em computadores, costuma ser 4 bytes.
<!--SR:!2024-10-29,4,270-->

Qual o resultado<br>![[Pasted image 20241025215616.png]];;A resposta é 5. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.
<!--SR:!2024-10-29,4,270-->

