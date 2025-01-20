Uma função, após ser inteiramente executada, pode por último retornar um valor a ser disponibilizado ao invocador. Este valor retornado deverá ter um tipo, por conta disso, `antes de definir uma função é necessário definir seu tipo!`
```C
#include <stdio.h>

float somar(float num1, float num2) {
	return num1 + num2;
}

int main(void) {
	printf("%.1f \n", somar(1.7, 1.3));
}
```

> Return finaliza e retorna um valor, logo, caso não seja a última instrução executada em uma função, tudo abaixo dele não será executado.

> [!WARNING] Uma função pode retornar APENAS UM valor.

>[!TIP] Após a instrução return pode ser colocada qualquer expressão válida em C.

Observe um possível uso do return:
```C
int max(int n1,int n2){

if (n1>n2)
	return n1;

else
	return n2;
}
```

---

## O "tipo" void
Podemos utilizar a palavra reservada - void - para indicar que a função em questão não retorna qualquer valor. Ainda é possível utilizar "return" como finalizadora, entretanto não retornará algo de fato.
>Ao não declarar um tipo, a função admite retorno inteiro. Ao indicar "void", o procedimento sequer possui um retorno.

Há também o uso do void para reforçar sobre a inexistência da presença de um parâmetro.

Por fim, adote como boa prática sempre o uso "semântico" nestes casos (principalmente em utilizar void quando não se utilizará o retorno de uma função).