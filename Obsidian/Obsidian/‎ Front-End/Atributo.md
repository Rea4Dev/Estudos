Dentro de um elemento, no caso aqui, a tag, podem haver atributos. Estes atributos trazem *especificações* e *modificações* para esta tag.

## *Exemplo de especificação*

![[Pasted image 20250315130509.png]]

Agora este elemento tag < p> possui um atributo **class** que *especifica* sua classe como sendo "destaque".

Previamente, o programador pode aplicar uma configuração que só afetará os atributos de classe destaque. Este é um exemplo do uso.

## *Exemplo de modificação*

````CSS
p{
	color:red;
	background-color: white;
	text-align:center;
}
````

<p style="color:red; background-color: white; text-align:center;">Exemplo</p>

Aprenderemos ainda sobre CSS (que trata da estilização), entretanto, vale por agora mostrar que é possível incluir o atributo **style** que irá permitir no valor do atributo incluir códigos CSS para modificar diretamente aquela tag em questão.

Neste exemplo, modificamos a cor do texto do parágrafo. 