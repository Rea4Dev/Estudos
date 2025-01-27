#flashcards/LinguagemC/Conceitual

C 1 - Como funciona, quando usar e quais as limitações do putchar();;![[Pasted image 20241212175933.png]]
<!--SR:!2025-02-04,15,297-->


C 2 - O que fazer para conseguir devidamente declarar caracteres especiais;;Sempre contra-barra, exceto operação com módulo, aí é duas %%%%  é o operador.
<!--SR:!2025-01-25,5,237-->


C 3 - O que significa o nome da função puts, qual suas diferenças em relação ao printf;;"put string"<br>(1)Inclui automaticamente quebra de linha no fim da string.<br>(2)Não é formatada.
<!--SR:!2025-02-04,15,297-->


C 4 - O que significa stdio;;Standard Input Output
<!--SR:!2025-02-04,15,297-->


C 5 - O que significa o .h;;Header files.
<!--SR:!2025-02-04,15,297-->


C 6 - stdio deve ser seguido de ponto e vírgula;;Não, pois não é uma instrução de C, assim como todos que começam com #, ele é uma diretiva ao pré-processador.
<!--SR:!2025-02-04,15,297-->


C 7 - Por que é printf e não print;;Pois printf = print + **formatado**.<br>Formatado pois, o uso do **%** e diversos outros artifícios (como %.2f) são possíveis pois printf é formatado.
<!--SR:!2025-02-04,15,297-->


C 8 - Quais os dois usos do caractere especial;;(1). Quando queremos representar um caractere que, de outro modo, seria difícil ou quase impossível de representar, como o \\n.<br>(2). Quando queremos retirar a especialidade de um caractere, como \ \.
<!--SR:!2025-01-31,11,277-->


C 9 - É possível comentários dentro de códigos?;;Sim, só não é recomendável.
<!--SR:!2025-02-04,15,297-->


C 10 - O que acontece quando declaramos uma variável;;Indicamos ao compilador para reservar um espaço na memória.
<!--SR:!2025-02-04,15,297-->


C 11 - Qual o tamanho em bytes de um int;;Na verdade, depende da arquitetura. Em microcontroladores, costuma ser 2 bytes - já em computadores, costuma ser 4 bytes.
<!--SR:!2025-02-04,15,297-->


C 12 - Qual o resultado<br>![[Pasted image 20241025215616.png]];;A resposta é 5. Quando são escritas várias atribuições consecutivas, estas são realizadas não da esquerda para a direita, mas sim da direita para a esquerda.
<!--SR:!2025-02-04,15,297-->



C 13 - Quais os operadores aritméticos em C;;\+  \-  \*  /  %
<!--SR:!2025-02-04,15,297-->


C 14 - Quais os outros formatos para inteiros;;%i para inteiro<br>%o para octal<br>%x para hexa<br>%X para hexa
<!--SR:!2025-01-27,7,257-->


C 15 - Qual operador disponibilizado pelo C para saber a dimensão de uma variável e como é sua declaração;;sizeof expressão<br>ou<br>sizeof(tipo)
<!--SR:!2025-01-31,11,277-->


C 16 - Para um inteiro de 2 bytes, qual o menor e qual o maior valor possível;;-32.768 | 32.767
<!--SR:!2025-02-04,15,297-->


C 17 - Para um inteiro de 4 bytes, qual o menor e qual o maior valor possível;;-2.147.483.648 | 2.147.483.647
<!--SR:!2025-01-29,7,277-->


C 18 - Para que serve o **short** em um **inteiro** e qual o operador;;Fixá-lo como 2 bytes independente da arquitetura. Operador %hd
<!--SR:!2025-02-04,15,297-->


C 19 - Para que serve o **long** em um **inteiro** e qual o operador;;Fixá-lo como 4 bytes independente da arquitetura. Operador %ld
<!--SR:!2025-02-04,15,297-->


C 20 - Para que serve o **signed** em um **inteiro** e qual o operador;;Incluir sinal, ou seja, não muda nada.
<!--SR:!2025-02-04,15,297-->


C 21 - Para que serve o **unsigned** em um **inteiro** e qual o operador;;Retirar sinal, ou seja, apenas positivos. Operador %u.<br>Obviamente, por consequencia, o valor máximo torna-se o dobro do que era.
<!--SR:!2025-01-25,3,217-->


C 22 - Qual os outros nomes para float e double;;Reais ou ponto flutuante
<!--SR:!2025-02-02,10,257-->


C 23 - Quais as diferenças de float e double;;Float ocupa 4 bytes, double ocupa 8
<!--SR:!2025-02-04,15,297-->


C 24 - Quais as precisões do Float e Double;;Float é dito precisão simples e double é dito precisão dupla
<!--SR:!2025-02-04,15,297-->


C 25 - Qual o resultado da operação de qualquer tipo com um real;;Resultado real.
<!--SR:!2025-02-04,15,297-->


C 26 - Quais os formatos de leitura que podem ser usados para pontos flutuantes;;%f<br>%e<br>%E
<!--SR:!2025-02-02,10,257-->


C 27 - Qual a quantidade de caracteres que o **char** consegue representar;;![[Pasted image 20241025115700.png]]
<!--SR:!2025-02-04,15,297-->

C 28 - Qual o formato de escrita do **char**;;<center style="font-size:180%">%c</center>
<!--SR:!2025-02-04,15,297-->



C 29 - Qual outra função usável no lugar de scanf para **char**;;<center>getchar()</center>
<!--SR:!2025-02-04,15,290-->


C 30 - Quantos caracteres **char** aguenta, quantos bytes é reservado e como é sua representação para o caractere *a*;;apenas um / 1 byte / 'a'
<!--SR:!2025-02-04,15,297-->


C 31 - \\n conta como caractere (sim ou não);;sim
<!--SR:!2025-02-04,15,297-->


C 32 - qual o problema clássico dos **char** e qual a solução;;armazenar dois char seguidos com scanf(). A solução para ter a resposta esperada é colocar um espaço antes do segundo %c.
<!--SR:!2025-02-04,15,297-->


C 33 - qual outra solução para o problema clássico dos **char**;;usar fflush(stdin) para limpar todos caracteres no buffer do teclado
<!--SR:!2025-02-04,15,297-->


C 34 - você lembra o porque do problema clássico dos **char**;;sim = fácil | não = difícil
<!--SR:!2025-02-04,15,297-->


C 35 - Comente sobre unsigned e signed char;;Por padrão, é unsigned. Entretanto, alguns famosos compiladores utilizam com sinal.<br>Continua sendo %c para todos os casos.
<!--SR:!2025-02-04,15,297-->





C 36 - Declare se há algo de errado com o código abaixo, e caso haja, corrija<br>![[Pasted image 20241025211419.png]];;Sim, há.<br>![[Pasted image 20241025211444.png]]
<!--SR:!2025-02-04,15,290-->




C 37 - De que forma fica uma variável declarada sem atribuir um valor a ela;;A variável assume um valor aleatório.
<!--SR:!2025-02-04,15,297-->


C 38 - Uma variável pode ser declarada e imediatamente atribuída \[Sim | Não]<br>![[Pasted image 20241031213313.png | center]];;Sim
<!--SR:!2025-02-04,15,297-->


C 39 - Qual a relação da natureza de um char e os inteiros;;As variáveis do tipo char não são mais do que pequenos inteiros guardados num único byte.<br>Assim, podem ser realizadas todas as operações numéricas que se podem realizar com inteiros.
<!--SR:!2025-02-04,15,297-->


C 40 - O que fazemos quando precisamos alterar uma determinada expressão para um determinado tipo;;Sempre que é necessário alterar uma expressão para um determinado tipo utiliza-se o casting (tipo). Essa alteração é temporária.<br>Não se deve realizar a leitura de variáveis de um determinado tipo usando um formato de leitura que não corresponda a esse tipo.
<!--SR:!2025-02-04,15,297-->








C 41 - O que representa o valor lógico FALSO e VERDADEIRO em C;;**0** = Falso<br>**Qualquer valor diferente de 0** = Verdadeiro
<!--SR:!2025-02-04,15,297-->


C 42 - Uma expressão que contenha um operador relacional devolve sempre como resultado o que;;O valor lógico *VERDADE* ou *FALSO*.
<!--SR:!2025-02-04,15,297-->


C 43 - Cite a respeito da Unicidade em estruturas condicionais;;![[Pasted image 20241106214937.png]]
<!--SR:!2025-02-04,15,297-->


C 44 - Por que este trecho de código está certo<br>![[Pasted image 20241106221307.png]];;Por que x é um valor diferente de zero, então escrever **x!=0** ou **x** da na mesma.<br>Entretanto, *não é recomendado usar apenas o x neste caso*, pois matamos uma fadinha do código limpo.
<!--SR:!2025-02-04,15,297-->


C 45 - A estrutura lógica não funcionou como esperado. Por quê? ![[Pasted image 20241111120106.png]];; Pois este código queria que o else fosse do primeiro IF, entretanto, sempre que existam instruções if-else encadeadas, cada else pertence sempre ao último if sem else.
<!--SR:!2025-02-04,15,290-->


C 46 - Lembra disso? ![[Pasted image 20241111123949.png]] ;; Se sim, OK ou Fácil<br>Se não, Difícil
<!--SR:!2025-02-04,15,290-->


C 47 - Ainda se lembra disso![[Pasted image 20241111135606.png]];;Se sim, OK ou Fácil<br>Se não, Difícil
<!--SR:!2025-01-31,11,277-->


C 48 - É possível fazer casting de modificador (como long, short, unsigned)? ;;<br>Sim. Todos podem ser feitos da forma como se espera (long), mas se constante pode ser colocado imediatamente depois do valor, como *3600***L**.
<!--SR:!2025-01-31,11,277-->


C 49 - Num if são necessários parênteses em torno da condição?;;Sim.
<!--SR:!2025-02-04,15,297-->


C 50 - O que é "corpo do laço"? ;; São as instruções dentro de um laço
<!--SR:!2025-02-04,15,297-->


C 51 - Para que serve utilizar %2d? ;; Propósito de alinhamento
<!--SR:!2025-02-04,15,297-->


![[Pasted image 20241105192112.png]]<br>C 52 - Isso funciona ou não;;Não
<!--SR:!2025-02-04,15,297-->

C 53 - Qual uma outra situação onde um Break pode ser empregado?;;Não só da forma usual, mas criativamente também em outras estruturas (tanto condicionais quanto de repetição) quando se deseja sair de toda a estrutura sem executar o restante.
<!--SR:!2025-02-07,16,309-->

C 54 - Qual a diferença do Break e do Continue?;;Break sai de toda a estrutura sem executar o restante. Aplicável em qualquer estrutura (seja condicional ou repetição).<br>Continue finaliza a iteração atual e executa o restante da estrutura passando para a próxima iteração. Aplicável somente em estruturas de repetição.
<!--SR:!2025-02-07,16,309-->

C 55 - O que acontece com um for(  ;  ;  )?;;É um loop infinito.![[Pasted image 20250116134726.png]]
<!--SR:!2025-02-07,16,309-->

C 56 - O que acontece com uma estrutura de repetição com a condição em branco?;;Quando no laço for não é colocada qualquer condição, esta é substituída por VERDADE.
<!--SR:!2025-01-31,11,289-->

C 57 - Onde deve ser definido o tipo de um parâmetro de função?;;Dentro dos parênteses da função<br>![[Pasted image 20250117194515.png | center]]
<!--SR:!2025-01-24,4,291-->
C 58 - Isso é permitido?<br>![[Pasted image 20250117201602.png]];;Sim
<!--SR:!2025-01-24,4,291-->

59 - Quantos valores pode retornar uma função?;;Apenas 1
<!--SR:!2025-01-24,4,291-->

60 - O que acontece quando não se declara o tipo de uma função?;;Ela assume int como tipo
<!--SR:!2025-01-24,4,291-->

61 - Pode-se definir funções dentro de funções?;;Não
<!--SR:!2025-01-25,4,271-->

62 - Podemos utilizar do retorno de uma função como argumento para outra função?<br>![[Pasted image 20250117201929.png]];;Sim
<!--SR:!2025-01-24,4,291-->

63 - Qual a diferença entre argumento e parâmetro?;;Argumento é passado na chamada, parâmetro é utilizado na função.
<!--SR:!2025-01-24,4,291-->

64 - Qual a diferença entre função e procedimento?;;Não há procedimentos em C, mas procedimento seria uma função sem retorno (logo, sem tipo também).
<!--SR:!2025-01-24,4,291-->

65 - Os nomes dos argumentos precisam ser o mesmo dos parâmetros?;;Não
<!--SR:!2025-01-24,4,291-->

66 - Por que definimos tipo de uma função?;;Na verdade, é o tipo do retorno.
<!--SR:!2025-01-24,4,291-->

67 - Isso é permitido?<br>![[Pasted image 20250117202518.png]];;Sim
<!--SR:!2025-01-24,4,291-->

68 - O que acontece ao chamar o return?;;A função deste return é finalizada e retorna o valor.
<!--SR:!2025-01-24,4,291-->

69 - Um procedimento ("tipo" void) pode ainda utilizar return como finalizador?;;Sim
<!--SR:!2025-01-26,4,308-->

70 - Em que podemos utilizar o void?;;Para declarar uma função sem retorno ou para reforçar a inexistência de parâmetros.
<!--SR:!2025-01-26,4,308-->

71 - Você sugere alguma alteração?<br>![[Pasted image 20250122155648.png]];;É melhor que utilize<br>![[Pasted image 20250122155706.png]]
<!--SR:!2025-01-26,4,308-->