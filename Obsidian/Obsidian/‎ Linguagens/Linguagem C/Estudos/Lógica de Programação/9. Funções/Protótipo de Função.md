Não há restrições quanto a declaração de uma função (se antes ou depois da função que a chamará ou da main). Entretanto, há uma situação em específico que pode causar `o problema das funções`:
```C
#include <stdio.h>

void main(){
	funcao();
}

void funcao(){
	printf("Hello, world!");
}
```


Por mais que a primeira vista o código acima pareça funcionar, não funciona. Ele apresenta o erro:
>[!WARNING] function funcao: redefinition

Este erro é devido a natureza do processo de compilação. Estando a função definida após a main, *quando o compilador compila a linha 4 ele ainda não a conhece*, `então cria um protótipo (cabeçalho) para ela`, semelhante a:
>[!NOTE] int funcao();

Entretanto, a função é void. Quando o compilador a encontra de fato, acaba entendendo que são distintas, apresentando o erro.

## Solução
Para solucionar, devemos adotar como boa prática criar protótipos para nossas funções. Protótipos garantem que o compilador irá estar ciente de qual será o tipo da função que ele encontrará, criando um protótipo adequado.

Para criar um protótipo, declare-o *logo após os includes* apenas com seu tipo seguido de seu nome e ";"
```C
#include <stdio.h>
void funcao();
```

>[!TIP] Sobre funções protótipo
>- O protótipo serve apenas para indicar ao compilador qual será o tipo, pois é isso que improta. Informações a respeito dos parâmetros não são relevantes.