#include <stdio.h>
#include "operacoes.h"

int escolher_validar(){
    int escolha;

    printf("Bem vindo a calculadora!\nInsira qual sera a operacao:");
    printf("\n\t[1]Adicao\n\t[2]Subtracao\n\t[3]Multiplicacao\n\t[4]Divisao\n");
    scanf("%d",&escolha);

    /* Validação */
    while(escolha != 1 && escolha != 2 && escolha != 3 && escolha != 4){
      printf("Opcao Invalida. Tente novamente: ");
      scanf("%d",&escolha);
    }

    return escolha;
}

int main(){
    int escolha;
    float resultado = 0;
    escolha = escolher_validar();

    switch (escolha){
    case 1:
        resultado = somar();
        printf("O resultado e %.1f",resultado);
        break;

    case 2:
        resultado = somar(); /* Basta inserir o número como negativo */
        printf("O resultado e %.1f",resultado);
        break;

    case 3:
        resultado = multiplicar();
        printf("O resultado e %.1f",resultado);
        break;

    case 4:
        resultado = dividir();
        printf("O resultado e %.1f",resultado);
        break;
    
    default:
        break;            
    }
}