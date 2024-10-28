Uma vez que estamos falando de números inteiros, é possível realizar um conjunto de operações sobre eles, cujo resultado é sempre um valor inteiro (ou seja, 7/3 faz sim sentido dar 2 aqui, pois int/int = int).
![[Pasted image 20241020135814.png]]

## Formato
Utilizamos formatos (juntamente a posterior referenciação de qual variável) para devidamente referenciar a posição de valores de variáveis.

> - "_O formato de escrita de um inteiro é **%d**_."

Para elucidar, analise a seguinte situação:

```
#include <stdio.h>

int main(void){

     int num1 = 123;

     printf(“O valor de num1 é num1”);

}
```

Veja que num1 está guardado numa variável, e não podemos colocar a variável num dentro da string do printf, uma vez que o printf iria escrever a string “num” em vez do valor que estaria guardado na variável.

Desta forma, para que conseguíssemos devidamente referenciar o valor da variável na posição, precisaríamos utilizar do formato %d e posteriormente colocamos por ordem as variáveis ou os valores que irão ser substituídos em cada %d, separados por vírgula. 

Da seguinte forma:

```
#include <stdio.h>

int main(void){

     int num1 = 123;

     printf(“O valor de num1 é %d”, num1);

}
```

## Outros formatos
Também é possível utilizar outros operadores para exibir o mesmo número em uma base diferente, tal como:
- **%i** para alternativa a %d
- **%o** para octal
- **%x** para hexa
- **%X** para hexa
```c
#include <stdio.h>

int main(){
    int num;
    scanf("%d",&num);

    printf("Em decimal: %d \n",num);
    printf("Em decimal: %i \n",num);

    printf("\nEm octal: %o \n",num);

    printf("\nEm hexa: %x \n",num);
    printf("Em hexa: %X \n",num);
}
```

---
# Revisão Espaçada
#flashcards/Logica_de_programação 

Quais os operadores aritméticos em C;;\+  \-  \*  /  %
<!--SR:!2024-10-29,4,270-->

Quais os outros formatos para inteiros;;%i para inteiro<br>%o para octal<br>%x para hexa<br>%X para hexa