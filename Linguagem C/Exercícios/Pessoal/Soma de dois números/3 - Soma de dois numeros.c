#include <stdio.h>

int captar(){
    float num1;
   
    printf("Insira o numero: ");
    scanf("%f",&num1);

    /* Retorno */
    return num1; /* Só é possível retornar um valor por vez */
}

float somar(){
    float num1, num2, resultado;

    /* Recebendo Retorno*/
    num1 = captar(); /* Esta é a forma de associar como queria */
    num2 = captar();
    
    /* Devolução final */
    return resultado = num1 + num2;
}

int main(){
    float resultado;

    puts("Bem vindo ao programa de somar dois!\n");

    resultado = somar();

    printf("O resultado da soma e: %2.f",resultado);
}