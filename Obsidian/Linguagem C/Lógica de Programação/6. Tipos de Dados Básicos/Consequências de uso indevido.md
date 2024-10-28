## Introdução
Apesar de se poder realizar conversões de inteiros para caracteres e vice-versa, *a leitura de inteiros com formato %c ou a leitura de caracteres com %d leva a resultados completamente inesperados e excepcionalmente perigosos*, <span style="color:red">não devendo por isso ser realizada</span>.
## Contra Exemplo 01 
O código abaixo ao entrar com 'A' esperava-se sair "65", entretanto, sai "833". 
Isso claramente é por conta do errôneo uso do "%". Entenda abaixo o porquê:

```c
#include <stdio.h>

main(){

  int num=1000;

  printf("Introduza um Caracter: ");

  scanf("%c",&num);

  printf("O valor de num = %d cujo caracter = '%c'\n", num,(char) num);
  
}
```
Se um inteiro ocupar dois bytes, os bits que representam o valor 1000 estão dispostos da seguinte forma:
<table> 

<thead> 
<tr> 
<th><center>int num = 1000;</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>0000 0011 | 1110 1000</center></td> 
</tr>
</tbody> 

</table>

>_"Quando se pede para ler um caractere (%c), a função scanf apenas vai alterar um byte em memória"._

Na linha 9 isso ocorre, então o caractere **'A'** cujo aspecto em binário é **0100 0001** ocupa o byte à direita
<table> 

<thead> 
<tr> 
<th><center>linha 9</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>0000 0011 | <span style="color:#54c5d1">0100 0001</span></center></td> 
</tr>
</tbody> 

</table>
$$
2^{^9}+2^{^8}+65=833
$$
Como consequência, ao inserir 'A' como entrada esperava-se ter '65', entretanto, pelos motivos visto acima, temos '833'. 

Concluímos que:

> _"Ao colocar o caractere lido num inteiro, apenas um dos bytes do inteiro será alterado, ficando num dos bytes o caractere lido. Todos os outros bytes componentes do inteiro ficam exatamente como estavam antes da chamada à função scanf"._

## Contra Exemplo 02
Observe os efeitos para entrada de "16706" que será armazenada no segundo char:
```c
#include <stdio.h>

main(){ 
  
  char ch1 = 'X', ch2 = 'Y';

  printf("Introduza um Inteiro: ");

  scanf("%d",&ch2);

  printf("O valor de ch1 = '%c' e ch2 = '%c'", ch1,ch2);

}
```

Embora não nos pareça lógica essa operação, é um erro muito comum e obtém-se como resultado a *alteração não apenas da variável ch2, mas também da variável ch1*.

Ao declarar duas variáveis do tipo char (ch1 e ch2), o compilador vai reservar *um byte para cada uma delas* e vai colocar os *bits* de cada uma delas de forma a que representem o caractere '*X*' e o caractere '*Y*'. Vamos supor que, por azar, as duas variáveis fiquem (como ficaram) uma depois da outra em memória.

![[Pasted image 20241024233800.png|center|300]]

Ao realizar uma *leitura de um inteiro* (%d), *independentemente* do *tipo* da *variável* que seja passada ao scanf, é <span style="color:#C82F4B">sempre alterado o número de bytes relativos a um inteiro</span>. Nesse caso, vão ser alterados **dois bytes** consecutivos.

Como foi enviada a variável **ch2** ao scanf, os *dois bytes que representam o inteiro vão ser armazenados a partir de ch2*. 

Como a variável **ch1** está imediatamente após a ch2, *ambas as variáveis vão ser alteradas pelo valor lido pelo scanf*, o <span style="color:#C82F4B">qual, separado em dois bytes, forma os números 65 e 66</span>, que representam os caracteres **ASCII** '**A**' e '**B**'.

>_A leitura de variáveis com a função scanf, utilizando formatos não adequados ao tipo das variáveis que são passadas, poderá levar a erros particularmente difíceis de detectar._

>_Os exemplos anteriores apresentaram os problemas de leitura de inteiros e caracteres com formatos incorretos. Tudo o que foi afirmado antes é válido para qualquer tipo de C (char, int, float ou double) em que se utilize a função scanf, com formatos não adequados às variáveis que vão receber cada um dos valores._
