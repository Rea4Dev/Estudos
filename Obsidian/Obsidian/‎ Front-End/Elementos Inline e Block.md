### _Diferença entre Elementos Inline e Block_

- **Elementos inline** ocupam apenas o espaço do seu conteúdo. Continuam na mesma linha, desde que haja espaço.
- **Elementos block** ocupam toda a largura disponível. Sempre começam em uma nova linha.
---

# Elementos Inline

Elementos inline ocupam apenas o espaço necessário para o seu conteúdo. Diferente dos elementos block, eles não quebram linha automaticamente e podem estar lado a lado em um mesmo espaço.

Os elementos inline são empilhados horizontalmente, um ao lado do outro, dentro de uma linha. Se o espaço não for suficiente, eles podem quebrar para a linha seguinte, mas sem alterar a estrutura do layout.

`Exemplos`
	_< span >_
	 _< a >_
	 _< img >_
	 _< strong >_
	 _< input >_
	 _< em >_
	 _< label >_

### _Margem e Padding_

As propriedades de margem e padding afetam o *espaço interno e externo* ao elemento, mas *não alteram sua largura ou altura*. Isso significa que, ao adicionar espaçamento a um elemento inline, ele não cresce verticalmente ou horizontalmente como um elemento block faria.

```CSS
span{
	padding: 20px;
	background-color: lightgray;
	color:black;
}
```

<span style="padding: 20px; background-color: lightgray; color:black;">Exemplo Visual</span>

### _Conversão entre Elementos Inline e Block_

No CSS, podemos alterar o comportamento padrão dos elementos utilizando a propriedade `display`. Por exemplo:

```css
span {
    display: block;
}
```

Isso faria com que um `<span>`, normalmente inline, se comportasse como um elemento block.

---

# Elementos Block

Os elementos block ocupam toda a largura disponível do contêiner pai e sempre iniciam em uma nova linha. Eles são usados principalmente para estruturar o layout da página.

Cada elemento block é renderizado em sua própria linha, abaixo do elemento anterior, formando um empilhamento vertical.

`Exemplo`
	_< div >_
	 _< p >_
	 _< h1 >, < h2 >, < h3 >, < h4 >, < h5 >, < h6 >_
	 _< ul >, < ol >, < li >_
	 _< section >_
	 _< article >_
	 _< form >_

### _Margem e Padding_

As propriedades de margem e padding _alteram a largura ou altura de um elemento block_, já que ele pode expandir para acomodar o conteúdo e os espaçamentos.

```CSS
div {
    padding: 20px;
    margin: 10px;
    background-color: lightgray;
    color: black;
}
```

<div style="padding: 20px; margin: 10px; background-color: lightgray; color: black;">Exemplo Visual</div>

As propriedades de _margem_ e _padding_ podem afetar tanto o espaço interno quanto o espaço externo de um elemento block, podendo alterar sua largura e altura.

### _Conversão entre Elementos Block e Inline_

Assim como elementos inline podem ser convertidos para block, também podemos transformar elementos block em inline:

```css
div {
    display: inline;
}
```

Isso faria com que uma `<div>`, normalmente block, se comportasse como um elemento inline, permitindo que ficasse ao lado de outros elementos na mesma linha.