/* Escreva a função x_isdigit, que verifica se um determinado caractere é dígito ou não. Escreva um programa de teste da função. */

#include <stdio.h>

void isdigit(char ch1) {
	return (ch1 >= '0' && ch1 <= '9') ? printf("Is digit") : printf("Is not a digit");
}

int main() {
	char ch1;
	printf("Input anything: ");
	ch1 = getchar();
	isdigit(ch1);
}