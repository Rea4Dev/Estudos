#flashcards/LinguagemC/Conceitual

C 1 - Como funciona, quando usar e quais as limitações do putchar();;![[Pasted image 20241212175933.png]]


C 2 - O que fazer para conseguir devidamente declarar caracteres especiais;;Sempre contra-barra, exceto operação com módulo, aí é duas %%%%  é o operador.


C 3 - O que significa o nome da função puts, qual suas diferenças em relação ao printf;;"put string"<br>(1)Inclui automaticamente quebra de linha no fim da string.<br>(2)Não é formatada.


C 4 - O que significa stdio;;Standard Input Output


C 5 - O que significa o .h;;Header files.


C 6 - stdio deve ser seguido de ponto e vírgula;;Não, pois não é uma instrução de C, assim como todos que começam com #, ele é uma diretiva ao pré-processador.


C 7 - Por que é printf e não print;;Pois printf = print + **formatado**.<br>Formatado pois, o uso do **%** e diversos outros artifícios (como %.2f) são possíveis pois printf é formatado.


C 8 - Quais os dois usos do caractere especial \\;;(1). Quando queremos representar um caractere que, de outro modo, seria difícil ou quase impossível de representar, como o \\n.<br>(2). Quando queremos retirar a especialidade de um caractere, como \\" \\".


C 9 - É possível comentários dentro de códigos?;;Sim, só não é recomendável.


C 10 - O que acontece quando declaramos uma variável;;Indicamos ao compilador para reservar um espaço na memória.


C 11 - Qual o tamanho em bytes de um int;;Na verdade, depende da arquitetura. Em microcontroladores, costuma ser 2 bytes - já em computadores, costuma ser 4 bytes.


C 12 - Qual o resultado<br>![[Pasted image 20241025215616.png]];;A resposta é 5. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.



C 13 - Quais os operadores aritméticos em C;;\+  \-  \*  /  %


C 14 - Quais os outros formatos para inteiros;;%i para inteiro<br>%o para octal<br>%x para hexa<br>%X para hexa


C 15 - Qual operador disponibilizado pelo C para saber a dimensão de uma variável e como é sua declaração;;sizeof expressão<br>ou<br>sizeof(tipo)


C 16 - Para um inteiro de 2 bytes, qual o menor e qual o maior valor possível;;32.768 | 32.767


C 17 - Para um inteiro de 4 bytes, qual o menor e qual o maior valor possível;;2.147.483.648 | 2.147.483.647


C 18 - Para que serve o **short** em um **inteiro** e qual o operador;;Fixá-lo como 2 bytes independente da arquitetura. Operador %hd


C 19 - Para que serve o **long** em um **inteiro** e qual o operador;;Fixá-lo como 4 bytes independente da arquitetura. Operador %ld


C 20 - Para que serve o **signed** em um **inteiro** e qual o operador;;Incluir sinal, ou seja, não muda nada.


C 21 - Para que serve o **unsigned** em um **inteiro** e qual o operador;;Retirar sinal, ou seja, apenas positivos. Operador %u.<br>Obviamente, por consequencia, o valor máximo torna-se o dobro do que era.


C 22 - Qual os outros nomes para float e double;;Reais ou ponto flutuante


C 23 - Quais as diferenças de float e double;;Float ocupa 4 bytes, double ocupa 8


C 24 - Quais as precisões do Float e Double;;Float é dito precisão simples e double é dito precisão dupla


C 25 - Qual o resultado da operação de qualquer tipo com um real;;Resultado real.


C 26 - Quais os formatos de leitura que podem ser usados para pontos flutuantes;;%f<br>%e<br>%E


C 27 - Qual a quantidade de caracteres que o **char** consegue representar;;![[Pasted image 20241025115700.png]]

C 28 - Qual o formato de escrita do **char**;;<center style="font-size:180%">%c</center>



C 29 - Qual outra função usável no lugar de scanf para **char**;;<center>getchar()</center>


C 30 - Quantos caracteres **char** aguenta, quantos bytes é reservado e como é sua representação para o caractere *a*;;apenas um / 1 byte / 'a'


C 31 - \\n conta como caractere (sim ou não);;sim


C 32 - qual o problema clássico dos **char** e qual a solução;;armazenar dois char seguidos com scanf(). A solução para ter a resposta esperada é colocar um espaço antes do segundo %c.


C 33 - qual outra solução para o problema clássico dos **char**;;usar fflush(stdin) para limpar todos caracteres no buffer do teclado


C 34 - você lembra o porque do problema clássico dos **char**;;sim = fácil | não = difícil


C 35 - Comente sobre unsigned e signed char;;Por padrão, é unsigned. Entretanto, alguns famosos compiladores utilizam com sinal.<br>Continua sendo %c para todos os casos.





C 36 - Declare se há algo de errado com o código abaixo, e caso haja, corrija<br>![[Pasted image 20241025211419.png]];;Sim, há.<br>![[Pasted image 20241025211444.png]]




C 37 - De que forma fica uma variável declarada sem atribuir um valor a ela;;A variável assume um valor aleatório.


C 38 - Uma variável pode ser declarada e imediatamente atribuída \[Sim | Não]<br>![[Pasted image 20241031213313.png | center]];;Sim


C 39 - Qual a relação da natureza de um char e os inteiros;;As variáveis do tipo char não são mais do que pequenos inteiros guardados num único byte.<br>Assim, podem ser realizadas todas as operações numéricas que se podem realizar com inteiros.


C 40 - O que fazemos quando precisamos alterar uma determinada expressão para um determinado tipo;;Sempre que é necessário alterar uma expressão para um determinado tipo utiliza-se o casting (tipo). Essa alteração é temporária.<br>Não se deve realizar a leitura de variáveis de um determinado tipo usando um formato de leitura que não corresponda a esse tipo.








C 41 - O que representa o valor lógico FALSO e VERDADEIRO em C;;**0** = Falso<br>**Qualquer valor diferente de 0** = Verdadeiro


C 42 - Uma expressão que contenha um operador relacional devolve sempre como resultado o que;;O valor lógico *VERDADE* ou *FALSO*.


C 43 - Cite a respeito da Unicidade em estruturas condicionais;;![[Pasted image 20241106214937.png]]


C 44 - Por que este trecho de código está certo<br>![[Pasted image 20241106221307.png]];;Por que x é um valor diferente de zero, então escrever **x!=0** ou **x** da na mesma.<br>Entretanto, *não é recomendado usar apenas o x neste caso*, pois matamos uma fadinha do código limpo.


C 45 - A estrutura lógica não funcionou como esperado. Por quê? ![[Pasted image 20241111120106.png]];; Pois este código queria que o else fosse do primeiro IF, entretanto, sempre que existam instruções if-else encadeadas, cada else pertence sempre ao último if sem else.


C 46 - Lembra disso? ![[Pasted image 20241111123949.png]] ;; Se sim, OK ou Fácil<br>Se não, Difícil


C 47 - Ainda se lembra disso![[Pasted image 20241111135606.png]];;Se sim, OK ou Fácil<br>Se não, Difícil


C 48 - É possível fazer casting de modificador (como long, short, unsigned)? ;;<br>Sim. Todos podem ser feitos da forma como se espera (long), mas se constante pode ser colocado imediatamente depois do valor, como *3600***L**.


C 49 - Num if são necessários parênteses em torno da condição?;;Sim.


C 50 - O que é "corpo do laço"? ;; São as instruções dentro de um laço


C 51 - Para que serve utilizar %2d? ;; Propósito de alinhamento


![[Pasted image 20241105192112.png]]<br>C 52 - Isso funciona ou não;;Não
