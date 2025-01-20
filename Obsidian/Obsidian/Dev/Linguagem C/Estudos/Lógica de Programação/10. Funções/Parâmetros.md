Ao chamar uma função, esta pode estar configurada a receber `argumentos`. Estes servem para serem utilizados como valores dentro da mesma.
```C
somar(1, 1)
```
Uma vez passado os argumentos para uma função, estes valores que podem ser utilizados denominam-se `parâmetros`, tendo seu nome e tipo definidos nela.
```C
int somar(int valor1, int valor2){
	int resultado = valor1 + valor2;
}
```
No caso abaixo, passamos um parâmetro que será uma variável de controle:
```C
#include <stdio.h>

linha(int num){
	int i;

	for (i=1 ; i<=num ; i++)
		putchar('*');
	putchar('\n');
}


main(){
	linha(3);
}
```
> O nome das variáveis (parâmetros) presentes no cabeçalho de uma função é totalmente independente do nome das variáveis que lhe serão enviadas pelo programa que a invoca.

> [!TIP] Qualquer expressão válida em C pode ser enviada como argumento para uma função.