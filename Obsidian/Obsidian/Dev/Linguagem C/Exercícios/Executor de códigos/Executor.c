#include <stdio.h>

void main() {
	int number;
	printf("Input a integer number: "); scanf_s("%d",&number);
	printf("\n\n %c",(char) number);
	printf("\n\n The next number is %d and the ASCII is %c", number + 1, (char)number + 1);
}