Quando estamos manipulando a entrada de dados do tipo char, é especialmente útil utilizar a função getchar() se possível pois esta é otimizada para este tipo de dado e situação. 
Ao utilizar o getchar(), você não precisa passar parâmetros adicionais.
```C
void x_isdigit() {
	char x;
	printf("Tipe something: ");
	x = getchar();
	printf("%c",x);
}
```

---
<center><h1>Uso alternativo</h1></center>
getchar() também possui um uso alternativo, este, associado a programas de terminal quando se deseja deixar com que o programa fique estabilizado esperando alguma ação (ou invés de simplesmente fechar). 

```C
#include <stdio.h>

int main(){
    char opcao;

    do{
        printf("\tM E N U    P R I N C I P A L\n");
        printf("\n\n\t\tClientes");
        printf("\n\n\t\tFornecedores");
        printf("\n\n\t\tEncomendas");
        printf("\n\n\t\tSair");
        printf("\n\n\n\t\t\tOpcao:");
        scanf(" %c", &opcao);

        fflush(stdin); /* Limpar o Buffer do teclado */

        switch (opcao){
             case 'c':
             case 'C': puts("Opcao CLIENTES"); break;
             case 'f':
             case 'F': puts("Opcao FORNECEDORES"); break;
             case 'e':
             case 'E': puts("Opcao ENCOMENDAS"); break;
             case 's':
             case 'S': break; /* Nao faz nada */
             default : puts("Opcao INVALIDA!!!");
          }
        getchar(); /* Parar a tela */
     }
    while (opcao!= 's' && opcao != 'S');
}
```