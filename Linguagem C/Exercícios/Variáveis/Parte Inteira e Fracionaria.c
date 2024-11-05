/*Escreva um programa em C que solicite um determinado número real e mostre qual a sua parte inteira e a sua parte fracionária.*/

#include <stdio.h>

int main(){
    float valor;
    scanf("%f",&valor);
    printf("\n Parte inteira:\t\t %d", (int) valor);
    printf("\n Parte fracionaria:\t %.2f", valor - ((int) valor) );
}