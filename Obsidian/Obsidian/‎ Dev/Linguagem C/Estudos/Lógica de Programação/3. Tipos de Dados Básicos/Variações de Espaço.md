Como foi mencionado anteriormente, o tamanho em bytes de um inteiro varia de arquitetura para arquitetura, sendo os valores mais habituais de 2 ou 4 bytes.

É importante saber qual a dimensão de um inteiro quando se desenvolve uma aplicação, caso contrário corre-se o risco de tentar armazenar um valor numa variável inteira com um nº de bytes insuficiente.

Para saber qual a dimensão de um inteiro (ou de qualquer tipo ou variável), o C disponibiliza um operador denominado sizeof, cuja sintaxe é semelhante à utilizada para invocar uma função.

A sintaxe do operador sizeof é:
```C
sizeof <expressão> ou sizeof ( <tipo> )
```

```c
#include <stdio.h>

main(){

     printf("O Tamanho em bytes de um Inteiro = %d\n", sizeof(int));

}
```

```C
main(){

	int myInt;
	printf("%lu\n", sizeof(myInt));
	
}
```