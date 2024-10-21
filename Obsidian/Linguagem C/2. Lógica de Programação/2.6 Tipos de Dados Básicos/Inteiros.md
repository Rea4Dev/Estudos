Uma vez que estamos falando de números inteiros, é possível realizar um conjunto de operações sobre eles, cujo resultado é sempre um valor inteiro.
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