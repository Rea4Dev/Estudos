#include <stdio.h>

int main(){
    /* Declaração de Variáveis Locais*/
    float num1 = 0, num2 = 0, resultado = 0;

    /*Saídas e Entradas*/
    printf("Insira o primeiro numero: ");
    scanf("%f",&num1);
    printf("Insira o segundo numero: ");
    scanf("%f",&num2);

    /* Soma */
    resultado = num1 + num2;

    /* Saída final */
    printf("O resultado e %.2f",resultado); /* Técnica de limitar casas decimais */
}