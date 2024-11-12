> _"Sempre que numa variável ou expressão temos um valor de um determinado tipo e queremos modificar o tipo desse valor, alterando-o para um tipo maior ou para um tipo mais baixo, podemos indicar o tipo ao qual queremos “promover” esse valor colocando o tipo pretendido entre parênteses antes do valor."_

Observe o caso abaixo que necessita correção:
```c
printf("O caractere %c tem o ASCII n° %d", ch, ch);
```
Devemos colocar o prefixo **(int)** para promover o valor da segunda variável **ch** temporariamente a inteiro antes de ser enviado para o printf (que espera um inteiro e não um char).
```c
printf("O caractere %c tem o ASCII n° %d", ch, (int) ch);
```

![[Pasted image 20241024222054.png | center]]

<center>Exemplo de um programa devidamente escrito:</center>
```c
#include <stdio.h>
main(){

    int num;
    
    scanf("%d",&num);

    printf("O num %d representa o caractere %c",num,(char) num);

    printf("\n\nO caractere seguinte %c tem o ascii %d", (char) (num+1) , num+1);

}
```

> _-"Sempre que é necessário alterar uma expressão para um determinado tipo utiliza-se o casting (tipo). Essa alteração é temporária."._

---
## Casting tamanho
A multiplicação entre dois inteiros devolve sempre um número inteiro. Caso quiséssemos que retornasse um long, teríamos que fazer o casting com pelo menos um dos valores operados.

Essa promoção pode ser realizada através de *(long)* ou colocando um L imediatamente após (se constante).

>seg = (hrs < 0) ? (0) : (n_horas * 3600L);