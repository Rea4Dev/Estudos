O tipo char permite armazenar um *único caractere* numa variável desse tipo.

No caso do char, independentemente da arquitetura utilizada, *sempre se armazena num único byte*.

Assim, o número de caracteres possíveis de representar é 256, pois é o número de combinações possíveis de representar num único byte (0…255).

<table> 

<thead> 
<tr> 
<th><center>Todos os bits com 0 (valor 0)</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>00000000</center></td> 
</tr>
</tbody> 

</table>

<table> 

<thead> 
<tr> 
<th><center>Todos os bits com 1 (valor 255)</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>11111111</center></td> 
</tr>
</tbody> 

</table>

Saiba da existência e uso do [[getchar( )]].
## Formato
O formato de escrita para o tipo *char* é **%c**.
> %c

```C
#include <stdio.h>

int main(){
    printf("%cello Wo%cld%c",'H','r','\n');
}
```
## Declaração
A declaração de uma variável do tipo char segue a sintaxe já conhecida:
```C
char nome = 'T'; 
```

A utilização de aspas para a representação de um caractere "A" é um *erro* comum, está totalmente incorreta e pode levar a algumas surpresas não muito agradáveis.

<table> 

<thead> 
<tr> 
<th><center>Nota pessoal</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>Por questão de bytes, busque inclusive utilizar char para colher opção de entrada do usuário ao invés de outros tipos que ocupem mais.</center></td> 
</tr>
</tbody> 

</table>

# Caracteres e Variações
Tal como o inteiro, um caractere também pode ser declarado com sinal (signed) ou sem sinal (unsigned).

Normalmente, *declarar uma variável do tipo char é equivalente a declarar uma variável do tipo unsigned char*, isto é, normalmente as variáveis do tipo char não têm sinal. No entanto, por padrão alguns compiladores muito utilizados (como é o caso dos compiladores da Borland Turbo C, Borland C etc.) utilizam os caracteres com sinal.
![[Pasted image 20241025224707.png | center]]

> _Quer seja signed ou unsigned, a leitura ou escrita de uma variável do tipo char, utilizando as funções scanf e printf, é sempre realizada com %c_.
# Char e caracteres especiais
Sabemos que o tipo char ocupa 1 byte e aceita apenas um caractere. Entretanto, os caracteres especiais são apenas 1 caractere, ou seja, " \\n" na verdade representa apenas 1 caractere!
```C
#include <stdio.h>

int main(){
    char A = '\n';
    printf("%c",A);
}
```

# Char e problema clássico
Observe o seguinte código para 'a' e 'b' como entradas:
```C
#include <stdio.h>

main(){ 
  
  char ch1, ch2;

  scanf("%c",&ch1);

  scanf("%c",&ch2);

  printf("Os caracteres introduzidos foram '%c' e '%c'\n", ch1,ch2);
}
```

<table> 

<thead> 
<tr> 
<th><center>Entrada</center></th> 
<th><center>Saída</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>a</center></td> 
<td>Os caracteres introduzidos foram 'a' e '
'</td> 
</tr>
</tbody> 

</table>

Não foi possível sequer chegar a inserir 'b', pois ao colocar 'a' o código exibe esta saída.
A razão, por mais que confusa a primeira vista, é a seguinte:

- (7) | '**a'** é digitado e **ENTER ↵** pressionado
O caractere 'a' é automaticamente colocado em ch1.

- (9) | o **ENTER ↵** anteriormente pressionado é armazenado no ch2 (ele também é um caractere)

Isso ocorre devido ao funcionamento sistêmico: 
Quando digitamos um caractere de entrada ele não é automaticamente registrado, é necessário pressionar ENTER ↵ para enviar. Isso é devido a presença do **buffer** responsável por este efeito.
Entretanto, ENTER ja é um caractere, ao pressioná-lo você inclui então dois caracteres:

>(1)  a

>(2) ↵

Quando enter participa da saída ele também gera a quebra de linha, aliás, ele é um \\n. 
Depois temos o ' e então, por fim, o último \\n.

## Solução
Para solucionar é simples, basta incluir um espaço em branco antes do _%c_ do segundo _scanf()_.

O espaço em branco dentro de um scanf *pede a essa função para ler e ignorar todos os Espaços em Branco, New Lines e Tabs* que encontrar.

```c
#include <stdio.h>

main(){ 
  
  char ch1, ch2;

  scanf("%c",&ch1);

  scanf(" %c",&ch2);

  printf("Os caracteres introduzidos foram '%c' e '%c'\n", ch1,ch2);
}
```

- Outra solução é utilizar o [[getchar( )]] ao invés de scanf().
- Uma outra forma de resolver o problema consiste em limpar todos os caracteres que existam no buffer do teclado utilizando a função **fflush(stdin)**;

# Natureza com inteiro

> -_"As variáveis do tipo char não são mais do que pequenos inteiros guardados num único byte. Assim, podem ser realizadas todas as operações numéricas que se podem realizar com inteiros."_


