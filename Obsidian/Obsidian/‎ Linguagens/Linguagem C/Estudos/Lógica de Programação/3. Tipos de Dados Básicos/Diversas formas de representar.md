Depois de declarada uma variável do tipo char existem diversas formas de colocar o caractere 'A' nessa variável.

```c
#include <stdio.h>

main(){
  char ch1 = 'A'; /*Formato tradicional*/
  printf("%c",ch1);

  char ch2 = 65; /*65 ASCII = A*/
  printf("%c",ch2);

  char ch3 = '\101'; /*65 ASCII em octal = 101*/
  printf("%c",ch3);

  char ch4 = '\x41'; /*65 ASCII em hexa = 41*/
  printf("%c",ch4);
}
```

<table> 

<thead> 
<tr> 
<th><center>Saída</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>AAAA</center></td> 
</tr>
</tbody> 

</table>

As quatro instruções anteriores são equivalentes, pois trabalhar em C com caracteres ou com o seu código ASCII é exatamente o mesmo.

Inclusive, mesmo que terrivelmente errado por diversos motivos (leia [[Casting, o uso correto]] e [[Consequências de uso indevido]]), observe no código abaixo que referenciar-se a um caractere por %d irá devolver seu código ASCII decimal:

```c
#include <stdio.h>

main(){

    char ch1 = 'A';
    
    printf("%d",ch1);

/*NÃO REPLIQUE ESTE CÓDIGO!*/

}
```

<table> 

<thead> 
<tr> 
<th><center>Saída</center></th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td><center>65</center></td> 
</tr>
</tbody> 

</table>

Entretanto, embora funcione, *não é ideal fazer os códigos desta forma* (leia [[Consequências de uso indevido]]), uma vez que o *%d está esperando um inteiro e não um caractere*. Para isso, será necessário modificar a estrutura usando o conceito de [[Casting, o uso correto]].
![[Pasted image 20241024220503.png | center]]
