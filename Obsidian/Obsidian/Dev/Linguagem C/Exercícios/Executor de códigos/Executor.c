#include <stdio.h>

void main() {
	float salario[12];
	float total = 0;
	for (int i = 0 ; i < 12 ; i++){
		printf("Insira o pagamento do mes %d: ", i+1);
		scanf_s("%f",&salario[i]);
		total = total + salario[i];
	}
	puts("Mes    |       Valor");
	for (int i = 0 ; i < 12 ; i++) {
		printf("\n%3.d %15.2f", i, salario[i]);
	}
	printf("\nTotal anual %.2f",total);
}