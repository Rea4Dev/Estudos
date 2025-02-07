Imagine que temos dois vetores e queremos utilizar uma função para preencher todas as posições do vetor com zero. 

``Natureza:``
	- O compilador *consegue saber o tipo* do vetor passado. Logo, mantenha o tipo do vetor passado correspondente ao tipo do vetor de parâmetro.
	- O compilador *não consegue saber a quantidade* no vetor passado. Logo, qualquer valor de quantidade informado no vetor de parâmetro é simplesmente ignorado.

```C
#include <stdio.h>

void inic(int vetor[],int quantidade){
	int i;
	for(i=0;i<quantidade;i++)
		vetor[i]=0;
}

main(){
	int vetor1[10];
	int Vetor2[20];
	
	inic(vetor1,10);
	inic(Vetor2,20);
}
```

Como o compilador não sabe a quantidade no vetor passado, ele não vai comparar com o que for colocado de quantidade no parâmetro - ignorando qualquer valor colocado -, o que nos possibilita gerar um *vetor genérico no parâmetro e operar com a quantidade de forma a parte*.
