Para ter acesso a esse conjunto de funções teremos que incluir a sua definição no nosso programa.

Neste caso, o #include <stdio.h>, que não é C, mas sim uma *diretiva que indica ao compilador (mais propriamente ao pré-processador) que deverá adicionar ao processo de compilação um arquivo existente em alguma parte no disco do seu computador*, chamado stdio.h, de forma que o compilador tenha acesso a um conjunto de informações sobre as funções que virá a utilizar.

Esses arquivos têm sempre a *extensão .h, pois não têm código,* mas apenas os cabeçalhos (headers) das funções que representam. São por isso habitualmente designados por *header files*.

Desse modo, a linha #include <stdio.h> significa ''adiciona o arquivo stdio.h ao meu programa''. Exatamente nessa posição. *Como não é uma instrução de C, não é seguida de ;*.

O arquivo stdio.h permite o acesso a todas as funções de entrada e saída normais; stdio quer dizer *standard input/output*.

As linhas começadas por # (#include, #define, etc.) não são C, mas sim diretivas ao pré-processador. Por isso não devem ser seguidas de ponto-e-vírgula.

---
# Revisão Espaçada

O que significa stdio;;Standard Input Output

O que significa o .h;;Header files.

stdio deve ser seguido de ponto e vírgula;;Não, pois não é uma instrução de C, assim como todos que começam com #, ele é uma diretiva ao pré-processador.