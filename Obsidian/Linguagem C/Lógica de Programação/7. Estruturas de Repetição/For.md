A instrução for adapta-se particularmente a situações em que o *número de iterações é conhecido a priori*. 
É um laço particularmente bem desenhado, que resume, em uma mesma instrução repetitiva, tudo aquilo de que ela necessita.

---

![[Pasted image 20241212180919.png]]

**1**. O código presente em cargas iniciais é executado. Normalmente aqui são iniciadas as variáveis presentes no laço. Esse componente do laço for é executado apenas uma única vez.

**2**. A condição é avaliada.

**3**. Se o resultado da condição retornar o valor Falso (zero), então o laço for termina e o programa continua na instrução imediatamente a seguir.

**4**. Se o resultado da condição retornar o valor Verdade, então é executada a instrução (ou bloco de instruções) do laço.

**5**. Depois de executada a instrução presente no laço, é executada a pós-instrução. Nesse componente do laço for são normalmente realizadas as alterações necessárias para passar à próxima iteração do laço (incremento ou decremento de variáveis etc.).

**6.** Voltar ao ponto 2.