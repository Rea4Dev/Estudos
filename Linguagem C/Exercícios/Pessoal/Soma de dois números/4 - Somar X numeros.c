#include <stdio.h>

float captar(){
    float num;
   
    printf("Insira o numero: ");
    scanf("%f",&num);

    /* Retorno */
    return num; /* Só é possível retornar um valor por vez */
}

float somar(){
    float num, resultado = 0; /* Cuidado com o lixo de memória */
    int quantidade, i;

    /* Recebendo Retorno*/
    printf("Quantos numeros quer somar?: ");
    scanf("%d",&quantidade);

    for (i = 0; i < quantidade; i++){
        num = captar();
        resultado += num;
        num = 0;
    }
    
    
    /* Devolução final */
    return resultado;
}

int main(){
    float resultado;

    puts("Bem vindo ao programa de somar dois!\n");

    resultado = somar();

    printf("O resultado da soma e: %2.f",resultado);
}