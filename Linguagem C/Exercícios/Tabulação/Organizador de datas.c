/*Escreva um programa que solicite ao usuário uma determinada data no formato aaaa-mm-dd e a mostre em seguida no formato dd/mm/aaaa.*/

#include <stdio.h>

int main(){
    int dia, mes, ano;

    printf("Escreva a data (no formato aaaa-mm-dd): ");
    scanf("%d-%d-%d", &ano, &mes, &dia);

    printf("\n A data ficou:\t %d/%d/%d", dia, mes, ano);
}