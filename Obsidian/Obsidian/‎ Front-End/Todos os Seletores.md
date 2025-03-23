Como já estudamos, os seletores definem os elementos HTML nos quais a regra CSS será aplicada.

Entretanto, há mais possibilidades de seletores além de serem diretamente as tags HTML. 

>[!Warning] Para Gabi
>Gabi, saiba que abaixo terão muitas formas diferentes. Peço para que preste especial atenção aos 6 primeiros, deles em diante peço apenas que passe o olho e saiba da existência.<br>
Não se assuste com o volume, por favor. Você inicialmente usará mais estes 6 primeiros, mas só de bater o olho e saber da existência dos demais, quando precisar, irá consultar aqui.

Veja abaixo:

---

## *1. Seletores de Tag (ou Tipo)*

Aplica o estilo diretamente a todas as tags daquele tipo.

**Exemplo:**

```css
p {
  color: blue;
}
```

```html
<p>Esse parágrafo ficará azul.</p>
```
---

### *2. Seletores de Classe ( . )*

Permite aplicar um estilo a elementos que possuam a classe especificada. 
Sendo classe, pode ser reutilizado em vários elementos.

**Exemplo:**

```css
.alerta {
  color: red;
}
```

```html
<p class="alerta">Este texto ficará vermelho.</p>
<div class="alerta">Esta div também ficará vermelha.</div>
```

---

### *3. Seletores de ID ( # )*

Aplica o estilo a um elemento específico que tenha aquele `id`. 
Sendo ID, deve ser único na página.

**Exemplo:**

```css
#titulo-principal {
  font-size: 32px;
}
```

```html
<h1 id="titulo-principal">Este título ficará maior.</h1>
```

---

### *4. Seletores Universais ( * )*

Aplica a regra a todos os elementos da página.

**Exemplo:**

```css
* {
  margin: 0;
  padding: 0;
}
```

---

## _5. Seletores de Grupo ( , )_

Permite aplicar o mesmo estilo a múltiplos elementos ao mesmo tempo, separando-os por vírgula.

**Exemplo:**

```css
h1, h2, p {
  font-family: Arial, sans-serif;
}
```

```html
<h1>Título principal</h1>
<h2>Subtítulo</h2>
<p>Este parágrafo também será afetado.</p>
```

Agora os elementos `<h1>`, `<h2>` e `<p>` terão a mesma fonte definida.

---
### *6. Seletores de Descendência (   )*

Aplica a regra a elementos que estão dentro de outro elemento.

>[!Warning]
O espaço entre os seletores pode afetar a performance em grandes documentos, pois ele verifica toda a árvore DOM.

**Exemplo:**

```css
div p {
  color: green;
}
```

```html
<div>
  <p>Este parágrafo dentro da div ficará verde.</p>
</div>
```
---
### *7. Seletores de Filho Direto ( > )*

Aplica a regra apenas aos elementos que são _filhos diretos_ do elemento pai.

>[!Tip]
Este seletor é útil quando se quer evitar a aplicação de estilos a elementos aninhados mais profundamente.

**Exemplo:**

```css
div > p {
  color: purple;
}
```

```html
<div>
  <p>Este parágrafo ficará roxo.</p>
  <div>
    <p>Este parágrafo não será afetado, pois não é filho direto da primeira div.</p>
  </div>
</div>
```

---

### *8. Seletores de Irmão Adjacente ( + )*

Aplica o estilo a um elemento que seja imediatamente adjacente a outro.

**Exemplo:**

```css
h1 + p {
  color: orange;
}
```

```html
<h1>Título</h1>
<p>Este parágrafo logo depois do h1 ficará laranja.</p>
<p>Este não será afetado.</p>
```

---

### *9. Seletores de Irmãos Gerais ( ~ )*

Aplica a regra a todos os elementos irmãos que vierem após o elemento indicado.

**Exemplo:**

```css
h1 ~ p {
  color: teal;
}
```

```html
<h1>Título</h1>
<p>Todos os parágrafos seguintes ficam verde-azulados.</p>
<p>Incluindo este.</p>
```

---

### *10. Seletores de Atributo ( \[ atributo ] )*

Permite selecionar elementos com determinados atributos. Especialmente útil quando não podemo/queremos alterar o HTML para colocar um atributo.

**Exemplo:**

```css
[required] {
  background-color: lightyellow;
}
```
```css
[type="text"] {
  background-color: lightyellow;
}
```
```css
input[type="text"] {
  background-color: lightyellow;
}
```

```html
<input type="text" required>
<input type="password">
```

---

### *11. Pseudo-classes ( : )*

Pseudo-classes lidam com estados ou posições do elemento. Utilizando : podemos aplicar regras CSS a elas.

![[Pasted image 20250322165341.png | center]]

**Exemplo:**

```css
a:hover {
  color: red;
}
```

Quando o usuário passa o mouse sobre o link, ele fica vermelho.

Outras pseudo-classes comuns:

- `:first-child`, `:last-child`, `:nth-child()`, `:checked`, etc.

Exemplo especial para nth-child (pois não é tão autodescritivo como os demais):

```CSS
<style>
  li:nth-child(odd) {
    background-color: grey;
  }

  li:nth-child(even) {
    background-color: azure;
  }
</style>
```

```CSS
<body>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
  </ul>
</body>
```
Basicamente, os itens ímpares da lista (`odd`) terão fundo *cinza (grey)* e os pares (`even`) terão fundo *azul claro (azure)*.

---

### *12. Pseudo-elementos ( :: )*

Pseudo-elementos lidam com partes do conteúdo. Permite estilizar partes específicas de um elemento.

**Exemplo:**
![[Pasted image 20250322172422.png]]
Veja que estamos alterando o conteúdo em questão sem ter que alterar o HTML. Novamente, também torna-se um alternativa para quando não podemos/queremos alterar no HTML.

Outros pseudo-elementos:

- `::before`, `::after`, `::first-line`, `::selection`.
