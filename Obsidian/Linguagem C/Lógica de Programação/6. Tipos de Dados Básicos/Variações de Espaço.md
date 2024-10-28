Como foi mencionado anteriormente, o tamanho em bytes de um inteiro varia de arquitetura para arquitetura, sendo os valores mais habituais de 2 ou 4 bytes.

É importante saber qual a dimensão de um inteiro quando se desenvolve uma aplicação, caso contrário corre-se o risco de tentar armazenar um valor numa variável inteira com um nº de bytes insuficiente.

Para saber qual a dimensão de um inteiro (ou de qualquer tipo ou variável), o C disponibiliza um operador denominado sizeof, cuja sintaxe é semelhante à utilizada para invocar uma função.

A sintaxe do operador sizeof é:
```
sizeof <expressão> ou sizeof ( <tipo> )
```

```
#include <stdio.h>

main(){

     printf("O Tamanho em bytes de um Inteiro = %d\n", sizeof(int));

}
```

---
# Revisão Espaçada
#flashcards/Logica_de_programação/espaço

Qual operador disponibilizado pelo C para saber a dimensão de uma variável e como é sua declaração;;sizeof expressão<br>ou<br>sizeof(tipo)
<!--SR:!2024-10-29,4,270-->