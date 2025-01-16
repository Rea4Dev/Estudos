No lugar da scanf, pode-se utilizar uma *outra função desenhada unicamente para a leitura de um caractere* — a função getchar().

A função getchar é invocada *sem qualquer parâmetro*. Ela lê um caractere e devolve o caractere obtido como resultado da função, evitando a escrita de parâmetros, formatos, &ch etc.

```C
#include <stdio.h>

int main(){

    char caractere;

    caractere = getchar();
  
    printf("%c",caractere);

}
```

