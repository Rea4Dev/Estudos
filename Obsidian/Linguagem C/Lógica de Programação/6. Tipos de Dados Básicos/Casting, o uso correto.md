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

---
# Revisão Espaçada
#flashcards/Logica_de_programação/variaveis/tipos/char 

Declare se há algo de errado com o código abaixo, e caso haja, corrija<br>![[Pasted image 20241025211419.png]];;Sim, há.<br>![[Pasted image 20241025211444.png]]

Faça um programa que colha um caractere digitado e mostre qual o código ASCII decimal dele e qual o caractere posterior a ele e também o código;;![[Pasted image 20241025211633.png]]