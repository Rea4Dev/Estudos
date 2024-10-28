#ifndef OPERACOES_H_INCLUDED
#define OPERACOES_H_INCLUDED

#include <stdio.h>

float captar(){
    float num;
   
    printf("Insira o numero: ");
    scanf("%f",&num);

    return num;
}

float somar(){ 
    int i, quantidade = 0;
    float resultado = 0, num = 0;

    printf("Insira quantos numeros quer operar: ");
    scanf("%d",&quantidade);

    for (i = 0; i < quantidade; i++){
        num = captar();
        resultado += num;
        num = 0;
    }
    return resultado;
}

float multiplicar(){
    int i, quantidade = 0;
    float resultado = 0, num = 0;

    printf("Insira quantos numeros quer operar: ");
    scanf("%d",&quantidade);

    resultado = captar(); /* Para evitar que multiplique por zero */
    for (i = 0; i < (quantidade -1); i++){
        num = captar();
        resultado *= num;
        num = 0;
    }
    return resultado;
}

float dividir(){
    int i, quantidade = 0;
    float resultado = 0, num = 0;

    printf("Insira quantos numeros quer operar: ");
    scanf("%d",&quantidade);

    resultado = captar(); /* Para evitar que multiplique por zero */
    for (i = 0; i < (quantidade -1); i++){
        num = captar();
        resultado /= num;
        num = 0;
    }
    return resultado;
}

#endif