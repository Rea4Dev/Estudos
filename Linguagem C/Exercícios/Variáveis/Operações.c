/*Escreva um programa em C que peça ao usuário dois inteiros e apresente o resultado da realização das operações aritméticas tradicionais.*/
#include <stdio.h>

int main(){
    int a, b;

    scanf("%d%d", &a, &b);
    
    printf("\n A soma de %d + %d = %d",a, b, a+b);
    printf("\n A subtracao de %d - %d = %d",a, b, a-b);
    printf("\n A multiplicacao de %d * %d = %d",a, b, a*b);
    printf("\n A divisao de %d / %d = %.1f",a, b, (float) a/b);
}