/* Escreva um programa em C que solicite um determinado número de segundos e, em seguida, indique quantas horas, minutos e segundos esse valor representa. */

#include <stdio.h>

int main(){
    /*Variáveis*/
    long int segundos;
    long int minutos;
    long int horas;

    /*Entrada*/
    scanf("%d",&segundos);
    
    /*Conversão*/
    horas = segundos/3600;
    minutos = segundos % 3600/60;
    segundos = segundos % 60;

    /*Saída*/
    printf("\n Equivale a %ld horas", horas);
    printf("\n Equivale a %ld minutos", minutos);
    printf("\n Equivale a %ld segundos", segundos);
}