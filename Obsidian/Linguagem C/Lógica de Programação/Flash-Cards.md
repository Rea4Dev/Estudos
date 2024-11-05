#flashcards/LinguagemC

O que fazer para conseguir devidamente declarar caracteres especiais;;Sempre contra-barra, exceto operação com módulo, aí é duas %%%%  é o operador.
<!--SR:!2024-11-09,4,295-->

O que significa o nome da função puts, qual suas diferenças em relação ao printf;;"put string"<br>(1)Inclui automaticamente quebra de linha no fim da string.<br>(2)Não é formatada.
<!--SR:!2024-11-14,15,290-->

O que significa stdio;;Standard Input Output
<!--SR:!2024-11-20,16,300-->

O que significa o .h;;Header files.
<!--SR:!2024-11-20,16,300-->

stdio deve ser seguido de ponto e vírgula;;Não, pois não é uma instrução de C, assim como todos que começam com #, ele é uma diretiva ao pré-processador.
<!--SR:!2024-11-20,16,300-->

Por que é printf e não print;;Pois printf = print + **formatado**.<br>Formatado pois, o uso do **%** e diversos outros artifícios (como %.2f) são possíveis pois printf é formatado.
<!--SR:!2024-11-14,15,290-->

Quais os dois usos do caractere especial \\;;(1). Quando queremos representar um caractere que, de outro modo, seria difícil ou quase impossível de representar, como o \\n.<br>(2). Quando queremos retirar a especialidade de um caractere, como \\" \\".
<!--SR:!2024-11-14,15,290-->

É possível comentários dentro de códigos?;;Sim, só não é recomendável.
<!--SR:!2024-11-14,15,290-->

O que acontece quando declaramos uma variável;;Indicamos ao compilador para reservar um espaço na memória.
<!--SR:!2024-11-10,11,270-->

Qual o tamanho em bytes de um int;;Na verdade, depende da arquitetura. Em microcontroladores, costuma ser 2 bytes - já em computadores, costuma ser 4 bytes.
<!--SR:!2024-11-14,15,290-->

Qual o resultado<br>![[Pasted image 20241025215616.png]];;A resposta é 5. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.
<!--SR:!2024-11-14,15,290-->


Quais os operadores aritméticos em C;;\+  \-  \*  /  %
<!--SR:!2024-11-14,15,290-->

Quais os outros formatos para inteiros;;%i para inteiro<br>%o para octal<br>%x para hexa<br>%X para hexa
<!--SR:!2024-11-07,3,240-->

Qual operador disponibilizado pelo C para saber a dimensão de uma variável e como é sua declaração;;sizeof expressão<br>ou<br>sizeof(tipo)
<!--SR:!2024-11-14,15,290-->

Para um inteiro de 2 bytes, qual o menor e qual o maior valor possível;;32.768 | 32.767
<!--SR:!2024-11-11,7,250-->

Para um inteiro de 4 bytes, qual o menor e qual o maior valor possível;;2.147.483.648 | 2.147.483.647
<!--SR:!2024-11-15,11,270-->

Para que serve o **short** em um **inteiro** e qual o operador;;Fixá-lo como 2 bytes independente da arquitetura. Operador %hd
<!--SR:!2024-11-15,11,270-->

Para que serve o **long** em um **inteiro** e qual o operador;;Fixá-lo como 4 bytes independente da arquitetura. Operador %ld
<!--SR:!2024-11-08,3,230-->

Para que serve o **signed** em um **inteiro** e qual o operador;;Incluir sinal, ou seja, não muda nada.
<!--SR:!2024-11-14,15,290-->

Para que serve o **unsigned** em um **inteiro** e qual o operador;;Retirar sinal, ou seja, apenas positivos. Operador %u.<br>Obviamente, por consequencia, o valor máximo torna-se o dobro do que era.
<!--SR:!2024-11-08,3,250-->

Qual os outros nomes para float e double;;Reais ou ponto flutuante
<!--SR:!2024-11-10,11,270-->

Quais as diferenças de float e double;;Float ocupa 4 bytes, double ocupa 8
<!--SR:!2024-11-14,15,290-->

Quais as precisões do Float e Double;;Float é dito precisão simples e double é dito precisão dupla
<!--SR:!2024-11-11,7,270-->

Qual o resultado da operação de qualquer tipo com um real;;Resultado real.
<!--SR:!2024-11-14,15,290-->

Quais os formatos de leitura que podem ser usados para pontos flutuantes;;%f<br>%e<br>%E
<!--SR:!2024-11-06,2,260-->

Qual a quantidade de caracteres que o **char** consegue representar;;![[Pasted image 20241025115700.png]]
<!--SR:!2024-11-20,16,300-->
Qual o formato de escrita do **char**;;<center style="font-size:180%">%c</center>
<!--SR:!2024-11-14,15,290-->


Qual outra função usável no lugar de scanf para **char**;;<center>getchar()</center>
<!--SR:!2024-11-14,15,290-->

Quantos caracteres **char** aguenta, quantos bytes é reservado e como é sua representação para o caractere *a*;;apenas um / 1 byte / 'a'
<!--SR:!2024-11-14,15,290-->

\\n conta como caractere (sim ou não);;sim
<!--SR:!2024-11-14,15,290-->

qual o problema clássico dos **char** e qual a solução;;armazenar dois char seguidos com scanf(). A solução para ter a resposta esperada é colocar um espaço antes do segundo %c.
<!--SR:!2024-11-14,15,290-->

qual outra solução para o problema clássico dos **char**;;usar fflush(stdin) para limpar todos caracteres no buffer do teclado
<!--SR:!2024-11-10,11,270-->

você lembra o porque do problema clássico dos **char**;;sim = fácil | não = difícil
<!--SR:!2024-11-14,15,290-->

Comente sobre unsigned e signed char;;Por padrão, é unsigned. Entretanto, alguns famosos compiladores utilizam com sinal.<br>Continua sendo %c para todos os casos.
<!--SR:!2024-11-20,16,300-->

Faça um programa com quatro variáveis char, fazendo com que as quatro devolva na saída o caractere A de maneiras diferentes. Descreva o nome de cada uma;;![[Pasted image 20241025210944.png]]
<!--SR:!2024-11-06,1,150-->

Declare se há algo de errado com o código abaixo, e caso haja, corrija<br>![[Pasted image 20241025211419.png]];;Sim, há.<br>![[Pasted image 20241025211444.png]]
<!--SR:!2024-11-20,16,300-->

Faça um programa que colha um número digitado e mostre qual a letra relativo ao código ASCII decimal dele - qual o caractere posterior a ele e também o código ASCII decimal;;![[Pasted image 20241025211633.png]]
<!--SR:!2024-11-09,4,295-->

De que forma fica uma variável declarada sem atribuir um valor a ela;;A variável assume um valor aleatório.
<!--SR:!2024-11-08,4,290-->

Uma variável pode ser declarada e imediatamente atribuída \[Sim | Não]<br>![[Pasted image 20241031213313.png | center]];;Sim
<!--SR:!2024-11-08,4,290-->

Qual a relação da natureza de um char e os inteiros;;As variáveis do tipo char não são mais do que pequenos inteiros guardados num único byte.<br>Assim, podem ser realizadas todas as operações numéricas que se podem realizar com inteiros.
<!--SR:!2024-11-08,4,290-->

O que fazemos quando precisamos alterar uma determinada expressão para um determinado tipo;;Sempre que é necessário alterar uma expressão para um determinado tipo utiliza-se o casting (tipo). Essa alteração é temporária.<br>Não se deve realizar a leitura de variáveis de um determinado tipo usando um formato de leitura que não corresponda a esse tipo.
<!--SR:!2024-11-08,4,290-->

Escreva um programa em C que solicite um determinado número real e mostre qual a sua parte inteira e a sua parte fracionária.;;![[Pasted image 20241105191213.png]]

![[Pasted image 20241105192112.png]]<br>Isso funciona ou não;;Não

Escreva um programa que solicite ao usuário uma determinada data no formato aaaa-mm-dd e a mostre em seguida no formato dd/mm/aaaa;;![[Pasted image 20241105193449.png]]