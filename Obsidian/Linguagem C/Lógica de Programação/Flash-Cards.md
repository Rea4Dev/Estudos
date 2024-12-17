#flashcards/LinguagemC

Como funciona, quando usar e quais as limitações do putchar();;![[Pasted image 20241212175933.png]]
<!--SR:!2024-12-20,4,321-->

O que fazer para conseguir devidamente declarar caracteres especiais;;Sempre contra-barra, exceto operação com módulo, aí é duas %%%%  é o operador.
<!--SR:!2024-12-19,8,295-->

O que significa o nome da função puts, qual suas diferenças em relação ao printf;;"put string"<br>(1)Inclui automaticamente quebra de linha no fim da string.<br>(2)Não é formatada.
<!--SR:!2025-01-18,60,310-->

O que significa stdio;;Standard Input Output
<!--SR:!2025-01-27,67,320-->

O que significa o .h;;Header files.
<!--SR:!2025-01-27,67,320-->

stdio deve ser seguido de ponto e vírgula;;Não, pois não é uma instrução de C, assim como todos que começam com #, ele é uma diretiva ao pré-processador.
<!--SR:!2025-01-08,48,300-->

Por que é printf e não print;;Pois printf = print + **formatado**.<br>Formatado pois, o uso do **%** e diversos outros artifícios (como %.2f) são possíveis pois printf é formatado.
<!--SR:!2025-01-18,60,310-->

Quais os dois usos do caractere especial \\;;(1). Quando queremos representar um caractere que, de outro modo, seria difícil ou quase impossível de representar, como o \\n.<br>(2). Quando queremos retirar a especialidade de um caractere, como \\" \\".
<!--SR:!2025-01-18,60,310-->

É possível comentários dentro de códigos?;;Sim, só não é recomendável.
<!--SR:!2025-01-18,60,310-->

O que acontece quando declaramos uma variável;;Indicamos ao compilador para reservar um espaço na memória.
<!--SR:!2024-12-22,41,290-->

Qual o tamanho em bytes de um int;;Na verdade, depende da arquitetura. Em microcontroladores, costuma ser 2 bytes - já em computadores, costuma ser 4 bytes.
<!--SR:!2025-01-18,60,310-->

Qual o resultado<br>![[Pasted image 20241025215616.png]];;A resposta é 5. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.
<!--SR:!2025-01-18,60,310-->


Quais os operadores aritméticos em C;;\+  \-  \*  /  %
<!--SR:!2025-01-18,60,310-->

Quais os outros formatos para inteiros;;%i para inteiro<br>%o para octal<br>%x para hexa<br>%X para hexa
<!--SR:!2024-12-25,36,280-->

Qual operador disponibilizado pelo C para saber a dimensão de uma variável e como é sua declaração;;sizeof expressão<br>ou<br>sizeof(tipo)
<!--SR:!2025-01-18,60,310-->

Para um inteiro de 2 bytes, qual o menor e qual o maior valor possível;;32.768 | 32.767
<!--SR:!2025-02-12,63,270-->

Para um inteiro de 4 bytes, qual o menor e qual o maior valor possível;;2.147.483.648 | 2.147.483.647
<!--SR:!2025-01-02,21,270-->

Para que serve o **short** em um **inteiro** e qual o operador;;Fixá-lo como 2 bytes independente da arquitetura. Operador %hd
<!--SR:!2024-12-30,41,290-->

Para que serve o **long** em um **inteiro** e qual o operador;;Fixá-lo como 4 bytes independente da arquitetura. Operador %ld
<!--SR:!2024-12-26,35,270-->

Para que serve o **signed** em um **inteiro** e qual o operador;;Incluir sinal, ou seja, não muda nada.
<!--SR:!2025-01-18,60,310-->

Para que serve o **unsigned** em um **inteiro** e qual o operador;;Retirar sinal, ou seja, apenas positivos. Operador %u.<br>Obviamente, por consequencia, o valor máximo torna-se o dobro do que era.
<!--SR:!2025-01-22,41,290-->

Qual os outros nomes para float e double;;Reais ou ponto flutuante
<!--SR:!2024-12-22,41,290-->

Quais as diferenças de float e double;;Float ocupa 4 bytes, double ocupa 8
<!--SR:!2025-01-18,60,310-->

Quais as precisões do Float e Double;;Float é dito precisão simples e double é dito precisão dupla
<!--SR:!2025-03-26,105,310-->

Qual o resultado da operação de qualquer tipo com um real;;Resultado real.
<!--SR:!2025-01-18,60,310-->

Quais os formatos de leitura que podem ser usados para pontos flutuantes;;%f<br>%e<br>%E
<!--SR:!2024-12-20,3,200-->

Qual a quantidade de caracteres que o **char** consegue representar;;![[Pasted image 20241025115700.png]]
<!--SR:!2025-01-27,67,320-->
Qual o formato de escrita do **char**;;<center style="font-size:180%">%c</center>
<!--SR:!2025-01-18,60,310-->


Qual outra função usável no lugar de scanf para **char**;;<center>getchar()</center>
<!--SR:!2025-01-18,60,310-->

Quantos caracteres **char** aguenta, quantos bytes é reservado e como é sua representação para o caractere *a*;;apenas um / 1 byte / 'a'
<!--SR:!2025-01-18,60,310-->

\\n conta como caractere (sim ou não);;sim
<!--SR:!2025-01-18,60,310-->

qual o problema clássico dos **char** e qual a solução;;armazenar dois char seguidos com scanf(). A solução para ter a resposta esperada é colocar um espaço antes do segundo %c.
<!--SR:!2025-01-18,60,310-->

qual outra solução para o problema clássico dos **char**;;usar fflush(stdin) para limpar todos caracteres no buffer do teclado
<!--SR:!2024-12-22,41,290-->

você lembra o porque do problema clássico dos **char**;;sim = fácil | não = difícil
<!--SR:!2025-01-18,60,310-->

Comente sobre unsigned e signed char;;Por padrão, é unsigned. Entretanto, alguns famosos compiladores utilizam com sinal.<br>Continua sendo %c para todos os casos.
<!--SR:!2025-01-15,35,300-->

Faça um programa com quatro variáveis char, fazendo com que as quatro devolva na saída o caractere A de maneiras diferentes. Descreva o nome de cada uma;;![[Pasted image 20241025210944.png]]
<!--SR:!2024-12-27,11,190-->

Declare se há algo de errado com o código abaixo, e caso haja, corrija<br>![[Pasted image 20241025211419.png]];;Sim, há.<br>![[Pasted image 20241025211444.png]]
<!--SR:!2025-01-27,67,320-->

Faça um programa que colha um número digitado e mostre qual a letra relativo ao código ASCII decimal dele - qual o caractere posterior a ele e também o código ASCII decimal;;![[Pasted image 20241025211633.png]]
<!--SR:!2025-02-19,70,335-->

De que forma fica uma variável declarada sem atribuir um valor a ela;;A variável assume um valor aleatório.
<!--SR:!2025-02-20,70,330-->

Uma variável pode ser declarada e imediatamente atribuída \[Sim | Não]<br>![[Pasted image 20241031213313.png | center]];;Sim
<!--SR:!2025-02-20,70,330-->

Qual a relação da natureza de um char e os inteiros;;As variáveis do tipo char não são mais do que pequenos inteiros guardados num único byte.<br>Assim, podem ser realizadas todas as operações numéricas que se podem realizar com inteiros.
<!--SR:!2025-02-18,69,330-->

O que fazemos quando precisamos alterar uma determinada expressão para um determinado tipo;;Sempre que é necessário alterar uma expressão para um determinado tipo utiliza-se o casting (tipo). Essa alteração é temporária.<br>Não se deve realizar a leitura de variáveis de um determinado tipo usando um formato de leitura que não corresponda a esse tipo.
<!--SR:!2025-02-18,69,330-->

Escreva um programa em C que solicite um determinado número real e mostre qual a sua parte inteira e a sua parte fracionária.;;![[Pasted image 20241105191213.png]]
<!--SR:!2025-02-11,61,317-->

![[Pasted image 20241105192112.png]]<br>Isso funciona ou não;;Não
<!--SR:!2024-12-19,8,297-->

Escreva um programa que solicite ao usuário uma determinada data no formato aaaa-mm-dd e a mostre em seguida no formato dd/mm/aaaa;;![[Pasted image 20241105193449.png]]
<!--SR:!2025-02-20,70,337-->

O que representa o valor lógico FALSO e VERDADEIRO em C;;**0** = Falso<br>**Qualquer valor diferente de 0** = Verdadeiro
<!--SR:!2025-02-20,70,337-->

Uma expressão que contenha um operador relacional devolve sempre como resultado o que;;O valor lógico *VERDADE* ou *FALSO*.
<!--SR:!2025-02-19,70,337-->

Cite a respeito da Unicidade em estruturas condicionais;;![[Pasted image 20241106214937.png]]
<!--SR:!2025-02-20,70,337-->

Por que este trecho de código está certo<br>![[Pasted image 20241106221307.png]];;Por que x é um valor diferente de zero, então escrever **x!=0** ou **x** da na mesma.<br>Entretanto, *não é recomendado usar apenas o x neste caso*, pois matamos uma fadinha do código limpo.
<!--SR:!2025-01-29,49,317-->

A estrutura lógica não funcionou como esperado. Por quê? ![[Pasted image 20241111120106.png]];; Pois este código queria que o else fosse do primeiro IF, entretanto, sempre que existam instruções if-else encadeadas, cada else pertence sempre ao último if sem else.
<!--SR:!2024-12-20,4,267-->

Lembra disso? ![[Pasted image 20241111123949.png]] ;; Se sim, OK ou Fácil<br>Se não, Difícil
<!--SR:!2024-12-28,16,307-->

Ainda se lembra disso![[Pasted image 20241111135606.png]];;Se sim, OK ou Fácil<br>Se não, Difícil
<!--SR:!2024-12-23,11,287-->

É possível fazer casting de modificador (como long, short, unsigned)? ;;<br>Sim. Todos podem ser feitos da forma como se espera (long), mas se constante pode ser colocado imediatamente depois do valor, como *3600***L**.
<!--SR:!2024-12-21,10,287-->

Num if são necessários parênteses em torno da condição?;;Sim.
<!--SR:!2024-12-24,8,307-->

O que é "corpo do laço"? ;; São as instruções dentro de um laço
<!--SR:!2025-01-03,18,337-->

Para que serve utilizar %2d? ;; Propósito de alinhamento
<!--SR:!2025-01-03,18,337-->