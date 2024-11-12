Da mesma forma que existe a função printf para a escrita de valores, existe uma função correspondente para a leitura de valores, a função scanf.
```
#include <stdio.h>

int main(){

     int num;

     printf(“Introduza um numero: “);

     scanf(“%d”,&num);

     printf(“O numero introduzido foi %d\n”,num);

}
```
No caso do programa anterior, queremos ler um valor para uma variável. Para tal usamos a função:
```
scanf()
```
O primeiro parâmetro dessa função é uma string com os formatos de leitura. Como só queremos ler uma variável, haverá apenas um formato de leitura. Sendo a variável que queremos ler do tipo inteiro, o formato de leitura será %d.
```
scanf("%d")
```
Em seguida, temos que indicar qual a variável que irá receber o valor inteiro a ser lido. Essa variável, como é do tipo inteiro, tem que levar um & antes de seu nome.
```
scanf("%d", &num);
```
e assim se obtém a linha 5, que permite realizar a leitura de um inteiro e armazená-lo numa variável.

O inteiro, depois de lido, é guardado na variável num e, em seguida, o seu valor é escrito na tela através da função printf.