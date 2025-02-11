As variáveis declaradas do tipo float ou double são utilizadas para armazenar valores numéricos com parte fracionária. São também frequentemente denominadas **reais** ou de **ponto flutuante**.

> O formato de leitura e escrita para números reais é %f, mas aceita também %e ou %E

Um float é representado por uma parte inteira e por outra decimal, separadas por um ponto (e não por uma vírgula — como é habitual em nosso uso do dia-a-dia).
![[Pasted image 20241023173935.png]]
## Diferenças
A diferença entre uma variável do tipo float e uma outra do tipo double é o *número de bytes que reserva para armazenar o valor*: 
- A dimensão do **float** é normalmente de *4 bytes*, enquanto a do **double** é de *oito bytes*. 
- Habitualmente pode-se dizer que esses dois tipos também armazenam números com **precisão simples** (float) ou com **dupla precisão** (double).

# Operações sobre reais
Qualquer operação que inclua um dos operandos do tipo real obtém um resultado do tipo real. A diferença entre um inteiro e um número real está na presença ou na ausência do ponto, que é o separador das partes inteira e fracionária.
![[Pasted image 20241023182408.png | center]]

O conjunto de operações disponíveis para os números de ponto flutuante é igual ao dos números inteiros (à exceção do operador % — Módulo).
![[Pasted image 20241023182541.png]]
