Uma variável deve ser sempre declarada antes de ser usada. A definição de uma variável indica ao compilador qual o tipo de dado que fica atribuído ao nome que indicarmos para essa variável.

A definição de variáveis é feita utilizando a seguinte sintaxe:
```
tipo nome;
```

Exemplos:
```
int num1;

char ch1, novo_char;

float pi, raio, perimetro;

double total, k123;
```

Como observado acima, é possível fazer declarações múltiplas de variáveis de mesmo tipo de uma só vez.

> -"_A declaração de variáveis tem que ser sempre realizada antes de sua utilização e antes de qualquer instrução_."


Uma variável pode ser declarada e imediatamente atribuída, também.
```c
#include <stdio.h>

int main(){

   int a=32;
   
}
```