#include <stdio.h>

void main(){
    float pagamentos[12];
    for (int i = 0; i < 12; i++){
        printf("Insira o valor do mes %d", i+1);
        scanf("%f",&pagamentos[i]);
    }
    printf("Os valores foram %f", pagamentos);
}