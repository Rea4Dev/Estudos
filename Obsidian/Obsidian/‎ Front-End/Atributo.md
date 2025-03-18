Dentro de um elemento, no caso aqui, a tag, podem haver atributos. Estes atributos trazem *especificações* e *modificações* para esta tag.

# Exemplo de especificação
![[Pasted image 20250315130509.png]]

Agora este elemento tag < p> possui um atributo **class** que *especifica* sua classe como sendo "destaque".

Previamente, o programador pode aplicar uma configuração que só afetará os atributos de classe destaque. Este é um exemplo do uso.

## Exemplo de modificação
````HTML
<p style="color:white">Texto branco</p>
````
Aprenderemos ainda sobre CSS (que trata da estilização), entretanto, vale por agora mostrar que é possível incluir o atributo **style** que irá permitir no valor do atributo incluir códigos CSS para modificar diretamente aquela tag em questão.

A este tipo de comportamento (estilizar diretamente a tag através do atributo style) chamamos de *CSS Inline*, algo como "CSS na linha", indicando que já é diretamente modificada a tag.

Neste exemplo, modificamos a cor do texto do parágrafo. 