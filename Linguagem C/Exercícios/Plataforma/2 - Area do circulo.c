/*
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

Exemplos de Entrada	
2.00

Exemplos de Saída
A=12.5664
*/

#include <stdio.h>
#include <math.h>

int main(){
    double pi = 3.14159, raio = 0, area = 0;
    scanf("%Lf",&raio);
    area = pi * (pow(raio, 2));
    printf("A=%.4Lf\n",area);
}