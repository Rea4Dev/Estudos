#include <stdio.h>

int main(){
	long long int num1;
	scanf("%ld",&num1);
	
	num1 = num1 * 200L;
    printf("\n %d", sizeof(num1));
}